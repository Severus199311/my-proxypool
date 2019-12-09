# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from ip66.items import Ip66Item


class A66ipSpider(Spider):
	name = '66ip'
	allowed_domains = ['www.66ip.cn']
	start_urls = ['http://www.66ip.cn/']

	def parse(self, response):
		urls = response.xpath('//ul[@class="textlarge22"]/li')
		if urls:
			for each in urls:
				url = each.xpath('./a/@href').extract_first()
				real_url = response.urljoin(url)
				yield Request(real_url, callback = self.parse_page)

	def parse_page(self, response):
		proxies = response.xpath('//div[@align="center"]/table/tbody/tr')
		print('为什么我永远抓不到proxies ？！！！', proxies)
		if proxies:
			for proxy in proxies:
				item = Ip66Item()
				ip = proxy.xpath('./td[1]/text()').extract_first()
				port = proxy.xpath('./td[2]/text()').extract_first()
				item['proxy'] = ip.strip() + ':' + port.strip()
				yield item