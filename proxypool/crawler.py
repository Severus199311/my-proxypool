from proxycrawlers.Kuaidaili import kuaidaili
from proxycrawlers.Jiangxianli import jiangxianli
from proxycrawlers.ip89 import ip89
from proxycrawlers.ip66 import ip66

class ProxyMetaclass(type):
	def __new__(cls, name, bases, attrs):
		#count = 0
		attrs['__CrawlFunc__'] = []
		for key, value in attrs.items():
			if 'crawler' in key:
				attrs['__CrawlFunc__'].append(key)
				#count += 1
		#attrs['__CrawlFuncCount__'] = count
		return type.__new__(cls, name, bases, attrs)

class Crawler(object, metaclass = ProxyMetaclass):
	def start_crawl_func(self, crawl_func):
		#proxies = []
		#for proxy in eval('self.{}()'.format(crawl_func)):
			#proxies.append(proxy)
		#return proxies
		return eval('self.{}()'.format(crawl_func))

		"""
	def crawler_kuaidaili(self):
		return kuaidaili.get_proxies()

	def crawler_jiangxianli(self):
		return jiangxianli.get_proxies()

	def crawler_ip89(self):
		return ip89.get_proxies()
		"""
	def crawler_ip66(self):
		return ip66.get_proxies()