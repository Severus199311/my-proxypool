import sys
sys.path.append(r'C:\Users\36328\web scraping\get_proxies\proxycrawlers')
from get_page import get_page
from lxml import etree
from pyquery import PyQuery as pq

def get_proxies():
	url = 'http://www.goubanjia.com/'
	html = get_page(url)
	if html:
		doc = pq(html)
		tr = doc('.table.table-hover tbody tr').items()
		for eachone in tr:
			td = eachone.children('.ip')
			proxy_fragments = td.children().text()
			proxy = proxy_fragments.replace(' ', '')
			print(proxy)

get_proxies()