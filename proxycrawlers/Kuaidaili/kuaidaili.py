from proxycrawlers.get_page import get_page
from lxml import etree
import time

def get_proxies():
	base_url = 'https://www.kuaidaili.com/free/inha/{}/'
	urls = [base_url.format(page) for page in range(1, 4)]
	for url in urls:
		html = etree.HTML(get_page(url))
		proxies = html.xpath('//*[@id="list"]/table/tbody/tr')
		for each in proxies:
			ip = each.xpath('./td[@data-title="IP"]/text()')[0]
			port = each.xpath('./td[@data-title="PORT"]/text()')[0]
			proxy = ip.strip() + ':' + port.strip()
			yield proxy
		time.sleep(1)