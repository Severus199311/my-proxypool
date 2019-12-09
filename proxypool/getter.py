from proxypool.crawler import Crawler
from proxypool.db import RedisClient
from settings import *


class Getter():
	def __init__(self):
		self.crawler = Crawler()
		self.redis = RedisClient()

	def run(self):
		if self.redis.count() < POOL_UPPER_THRESHOLD:
			#for crawl_func_label in range(self.crawler.__CrawlFuncCount__):
			for crawl_func in self.crawler.__CrawlFunc__:
				#crawl_func = self.crawler.__CrawlFunc__[crawl_func_label]
				proxies = self.crawler.start_crawl_func(crawl_func)
				print(crawl_func, '正在爬取代理')
				for proxy in proxies:
					print(proxy)
					self.redis.add(proxy)
		proxy_sum = self.redis.count()
		print('目前代理个数：', proxy_sum)