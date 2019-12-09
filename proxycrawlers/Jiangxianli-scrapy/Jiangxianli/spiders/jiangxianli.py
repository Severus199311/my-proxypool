# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from Jiangxianli.items import JiangxianliItem


class JiangxianliSpider(Spider):
	name = 'jiangxianli'
	allowed_domains = ['ip.jiangxianli.com']
	start_urls = ['http://ip.jiangxianli.com/']

	def parse(self, response):
		proxies = response.xpath('//*[contains(@class, "table") and contains(@class, "table-hover") and contains(@class, "table-border") and contains(@class, "table-striped")]/tbody/tr')
		for proxy in proxies:
			item = JiangxianliItem()
			ip = proxy.xpath('./td[2]/text()').extract_first()
			port = proxy.xpath('./td[3]/text()').extract_first()
			item['proxy'] = ip.strip() + ':' + port.strip()
			yield item

		if response.xpath('//ul[@class="pagination"]/li[@class="active"]/following-sibling::li/a/@href'):
			next_page_url = response.xpath('//ul[@class="pagination"]/li[@class="active"]/following-sibling::li/a/@href').extract_first()
			yield Request(url = next_page_url, callback = self.parse)


