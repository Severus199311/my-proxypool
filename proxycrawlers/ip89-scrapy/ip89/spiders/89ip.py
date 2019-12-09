# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from ip89.items import Ip89Item


class A89ipSpider(Spider):
	name = '89ip'
	allowed_domains = ['www.89ip.cn']
	start_urls = ['http://www.89ip.cn/']

	def parse(self, response):
		proxies = response.xpath('//*[@class="layui-table"]/tbody/tr')
		if proxies:
			for proxy in proxies:
				item = Ip89Item()
				ip = proxy.xpath('./td[1]/text()').extract_first()
				port = proxy.xpath('./td[2]/text()').extract_first()
				item ['proxy'] = ip.strip() + ':' +port.strip()
				yield item

			next_page = response.xpath('//*[@class="layui-laypage-next"]/@href').extract_first()
			next_page_url = response.urljoin(next_page)
			yield Request(next_page_url, callback = self.parse)