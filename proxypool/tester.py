from proxypool.db import RedisClient
from settings import *
import aiohttp
import asyncio
import time
from asyncio import TimeoutError
try:
	from aiohttp import ClientError
except:
	from aiohttp import ClientProxyConnectionError as ProxyConnectionError

class Tester(object):
	def __init__(self):
		self.redis = RedisClient()

	async def test_single_proxy(self, proxy):
		conn = aiohttp.TCPConnector(ssl = False)
		async with aiohttp.ClientSession(connector = conn) as session:
			try:
				if isinstance(proxy, bytes):
					proxy = proxy.decode('utf-8')
				real_proxy = 'http://' + proxy
				async with session.get(TEST_URL, proxy = real_proxy, timeout = 15, allow_redirects=False) as response:
					print('正在测试', proxy)
					if response.status in VALID_STATUS_CODES:
						self.redis.max(proxy)
						print('代理可用', proxy)
					else:
						self.redis.decrease(proxy)
						print('请求响应码不合法', proxy)
			except (ClientError, aiohttp.client_exceptions.ClientConnectorError, TimeoutError, AttributeError):
				self.redis.decrease(proxy)
				print('代理请求失败', proxy)

	def run(self):
		proxy_sum = self.redis.count()
		proxies= self.redis.all()
		print('待检测代理个数', proxy_sum)
		try:
			for batch_limit in range(0, proxy_sum, BATCH_TEST_SIZE):
				start = batch_limit
				stop = min(batch_limit + BATCH_TEST_SIZE, proxy_sum)
				print('当前正在检测代理第', start + 1, '至第', stop, '个')
				proxy_batch = proxies[start: stop]
				loop = asyncio.get_event_loop()
				tasks = [self.test_single_proxy(proxy) for proxy in proxy_batch]
				loop.run_until_complete(asyncio.wait(tasks))
				time.sleep(5)
		except Exception as e:
			print('测试器发生错误', e.args)