import sys
sys.path.append(r'C:\Users\36328\web scraping\get_proxies\proxycrawlers')
from get_page import get_page
from lxml import etree
import requests
from urllib.parse import quote


class Zdaye_Crawler():
	def __init__(self):
		self.login_page_headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
		}
		self.logined_page_headers = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
			'Cache-Control': 'max-age=0',
			'Connection': 'keep-alive',
			'Content-Length': '83',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Host': 'www.zdaye.com',
			'Origin': 'https://www.zdaye.com',
			'Referer': 'https://www.zdaye.com/Users/Login.html',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site': 'same-origin',
			'Sec-Fetch-User': '?1',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
		}
		self.logined_page_form_data = {
			'usernamePH': '15757120656',
			'passwordPH': 'sxy199311',
			'login': '1',
			'autoLogin': '1'
		}
		self.login_page_url = 'https://www.zdaye.com/Users/Login.html'
		self.logined_page_url = 'https://www.zdaye.com/Users/Login.html'
		#self.logined_page_url = 'https://www.zdaye.com/Users/index_15757120656.html'
		#self.logined_page_url = 'https://www.zdaye.com/ok.html?o=' + quote('恭喜您，登陆成功') + '&u=C600D6008600F50063005300630003002300130073005300730053001300F500870056004600E6009600F20037002700560037005500F20077007600&t=2'
		self.session = requests.Session()

	def get_login_page(self):
		self.session.get(self.login_page_url, headers = self.login_page_headers, verify = False)

	def get_logined_page(self):
		self.session.post(self.logined_page_url, data = self.logined_page_form_data, headers = self.logined_page_headers, verify = False)

	def run(self):
		self.get_login_page()
		response = self.get_logined_page()
		print(response.text)

crawler = Zdaye_Crawler()
crawler.run()