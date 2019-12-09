import sys
sys.path.append(r'C:\Users\36328\web scraping\get_proxies\proxycrawlers')
from get_page import get_page
import re
from lxml import etree


headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': 'UM_distinctid=16e2c2c9e2926c-0ccd9b2f68a2f4-67e1b3f-e1000-16e2c2c9e2a2ab; Qs_lvt_104358=1572780421; Qs_pv_104358=3428592927462810000; Hm_lvt_3406180e5d656c4789c6c08b08bf68c2=1572699152,1572699395,1572780421,1572859749; JSESSIONID=424747985DA8A6C17AD912741C64132E; CNZZDATA1260383977=1360224433-1572696207-null%7C1572864721; gdt_fp=e12ea86fcb656edde92ab27ee79fe947; Hm_lpvt_3406180e5d656c4789c6c08b08bf68c2=1572866727',
	'Host': 'http://www.data5u.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

def get_proxies():
	url = 'http://www.data5u.com'
	html = etree.HTML(get_page(url))
	ul_list = html.xpath('//ul[@class = "l2"]')
	for ul in ul_list:
		host_span = etree.tostring(ul.xpath('./span[1]')[0]).decode('utf-8')
		port_span = etree.tostring(ul.xpath('./span[2]')[0]).decode('utf-8')
		proxy = re.match('<span><li>(.*?)<\/li><\/span>', host_span, re.S).group(1)
		port = re.match('<span style="width: 100px;"><li class="port.*?">(.*?)<\/li><\/span>', port_span, re.S).group(1)
		print(proxy, port)

get_proxies()