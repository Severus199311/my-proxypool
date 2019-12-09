from pyquery import PyQuery as pq
import sys
sys.path.append(r'C:\Users\36328\web scraping\get_proxies\proxycrawlers')
from get_page import get_page
import re
from urllib.parse import urljoin

def get_urls():
	entrance_url = 'http://www.66ip.cn'
	html = get_page(entrance_url)
	if html:
		doc = pq(html)
		url_table = doc('.textlarge22')
		url_table('li:first-child').remove()
		urls = url_table.children().items()
		for each in urls:
			href = each.children('a').attr('href')
			url = urljoin(entrance_url, href)
			yield url

def parse_urls(url):
	html = get_page(url)
	if html:
		doc = pq(html)
		proxy_table = doc('#footer div table')
		proxy_table('tr:first-child').remove()
		proxies = proxy_table.children().items()
		for each in proxies:
			each = str(each)
			ip = re.match('<tr><td>(.*?)<\/td><td>(.*?)<\/td><td>', each, re.S).group(1).strip()
			port = re.match('<tr><td>(.*?)<\/td><td>(.*?)<\/td><td>', each, re.S).group(2).strip()
			proxy = ip + ':' + port
			yield proxy

def get_proxies():
	urls = get_urls()
	for url in urls:
		proxies = parse_urls(url)
		if proxies:
			for proxy in proxies:
				yield proxy

