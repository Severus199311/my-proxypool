import sys
sys.path.append(r'C:\Users\36328\web scraping\get_proxies\proxycrawlers')
from get_page import get_page
from lxml import etree

def get_proxies():
	url = 'http://www.iphai.com/'
	html = etree.HTML(get_page(url))
	print(html.text)
	proxies = html.xpath('/html/body/div[4]/div[2]/table/tbody/tr')
	for each in proxies:
		ip = each.xpath('./td[1]/text()')[0]
		port = each.xpath('./td[2]/text()')[0]
		proxy = ip.strip() + ':' + port.strip()
		print(proxy)

get_proxies()