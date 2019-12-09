from proxycrawlers.get_page import get_page
from lxml import etree

def get_proxies():
	base_url = 'http://ip.jiangxianli.com/?page={}'
	urls = [base_url.format(page) for page in range(1, 3)]
	for url in urls:
		html = etree.HTML(get_page(url))
		proxies = html.xpath('/html/body/div[1]/div/div[1]/div[2]/table/tbody/tr')
		for each in proxies:
			ip = each.xpath('./td[2]/text()')[0]
			port = each.xpath('./td[3]/text()')[0]
			proxy = ip.strip() + ':' + port.strip()
			yield proxy