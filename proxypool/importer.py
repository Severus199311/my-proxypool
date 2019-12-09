from proxypool.db import RedisClient

conn = RedisClient()

def set(proxy):
	result = conn.add(proxy)
	print(proxy, '录入成功' if result else '录入失败')

def scan():
	while True:
		proxy = input('请输入代理，或输入exit退出:')
		if proxy == 'exit':
			break
		set(proxy)