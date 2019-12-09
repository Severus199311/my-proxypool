from proxycrawlers.get_page import get_page
from lxml import etree

def get_proxies():
	base_url = 'http://www.89ip.cn/index_{}.html'
	urls = [base_url.format(page) for page in range(1, 24)]
	for url in urls:
		html = etree.HTML(get_page(url))
		proxies = html.xpath('//*[@class="layui-table"]/tbody/tr')
		for each in proxies:
			ip = each.xpath('./td[1]/text()')[0]
			port = each.xpath('./td[2]/text()')[0]
			proxy = ip.strip() + ':' + port.strip()
			yield proxy