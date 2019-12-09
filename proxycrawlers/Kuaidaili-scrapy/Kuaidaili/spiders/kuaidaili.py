# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from Kuaidaili.items import KuaidailiItem
import time

class KuaidailiSpider(Spider):
	name = 'kuaidaili'
	allowed_domains = ['www.kuaidaili.com']
	start_urls = ['https://www.kuaidaili.com/free/']

	def parse(self, response):
		proxies = response.xpath('//*[@id="list"]/table/tbody/tr')
		if proxies:
			for proxy in proxies:
				fresh_proxy = self.fresh_proxy(proxy)
				if fresh_proxy:
					item = KuaidailiItem()
					ip = proxy.xpath('./*[@data-title="IP"]/text()').extract_first()
					port = proxy.xpath('./*[@data-title="PORT"]/text()').extract_first()
					item['proxy'] = ip.strip() + ':' + port.strip()
					yield item
				else:
					break

			last_proxy_of_the_page = response.xpath('//*[@id="list"]/table/tbody/tr[last()]')
			fresh_proxy = self.fresh_proxy(proxy)
			if fresh_proxy:
				next_page = response.xpath('//*[@id="listnav"]/ul//*[@class="active"]/../following-sibling::li[1]/a/@href').extract_first()
				next_page_url = response.urljoin(next_page)
				print('下一个爬取的URL是', next_page_url)
				yield Request(next_page_url, callback=self.parse)

	def fresh_proxy(self, proxy):
		last_check = proxy.xpath('./td[@data-title="最后验证时间"]/text()').extract_first().strip()
		last_check_struct_time = time.strptime(last_check, '%Y-%m-%d %H:%M:%S')
		last_check_time_stamp = time.mktime(last_check_struct_time)
		fresh_proxy = time.time() - last_check_time_stamp < 24 * 60 * 60
		return fresh_proxy
