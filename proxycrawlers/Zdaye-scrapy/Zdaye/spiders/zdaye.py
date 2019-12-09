# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from Zdaye.items import ZdayeItem
import re


class ZdayeSpider(Spider):
	name = 'zdaye'
	allowed_domains = ['www.zdaye.com']
	start_urls = ['https://www.zdaye.com/dayProxy.html']

	def parse(self, response):
		#urls = response.xpath('//*[@class="thread_item"]') 
		urls = response.xpath('//*[@id="J_posts_list"]/div[@class="thread_item"]')
		print('吹吹牛随你城市对成本女', urls)
		for each in urls:
			url = each.xpath('./div[@class="thread_content"]/div[@class="thread_title"]/a/@href').extract_first()
			real_url = response.urljoin(url)
			print('拉拉的成本一般超声波测完',real_url)
			yield Request(real_url, callback=self.parse_page)

	def parse_page(self, response):
		proxies = response.xpath('//*[@class="cont"]/br')
		for proxy in proxies:
			item = ZdayeItem()
			item['proxy'] = proxy.xpath('./text()').re('\d+\.\d+\.\d+\.\d+:\d+').extract_first()
			yield item