from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from pyquery import PyQuery as pq
from urllib.parse import urljoin
import re
from time import time, localtime, strftime

class ZdayeCrawler():
	def __init__(self):
		self.chrome_options = webdriver.ChromeOptions()
		self.prefs = {'profile.managed_default_content_settings.images': 2}
		self.chrome_options.add_experimental_option('prefs', self.prefs)
		self.chrome_options.add_argument('--headless')
		self.browser = webdriver.Chrome(chrome_options = self.chrome_options)
		self.browser.set_window_size(1400, 700)
		self.wait = WebDriverWait(self.browser, 10)
		#self.login_url = 'https://www.zdaye.com/Users/Login.html'
		self.IPList_url = 'https://www.zdaye.com/FreeIPList.html'
		self.username = '15757120656'
		self.password = 'sxy199311'

	def get_page(self):
		try:
			"""self.browser.get(self.login_url)
			username_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.dlbox.ov > div > form > div.dl.ov > p:nth-child(1) > input[type=text]')))
			password_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.dlbox.ov > div > form > div.dl.ov > p:nth-child(2) > input[type=password]')))
			username_input.send_keys(self.username)
			password_input.send_keys(self.password)
			login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.dlbox.ov > div > form > div.dl.ov > strong > input[type=submit]')))
			login_button.click()"""
			self.browser.get(self.IPList_url)
			IPList_page = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.header.bg > div > ul > li:nth-child(5) > a')))
			IPList_page.click()
			return self.browser.page_source
		except TimeoutException:
			self.get_page()

	def get_ips(self):
		html = self.get_page()
		doc = pq(html)
		tr = doc('#ipc > tbody > tr:nth-child(1)')
		proxy = tr('td:first-child').text()
		img = tr.find('img')
		src = img.attr('src')
		port_url = urljoin(self.IPList_url, src)
		return {
			'proxy': proxy,
			'port_url': port_url
		}

	def get_images(self):
		ip_info = self.get_ips()
		proxy = ip_info.get('proxy')
		port_url_old = ip_info.get('port_url')
		port_url_fragment = re.match('(.*gif\?).*', port_url_old).group(1)
		current_time = strftime('%Y/%m/%d %H:%M:%S', localtime(time()))
		port_url_new = port_url_fragment + current_time
		try:
			self.browser.get(port_url_new)
			port = self.browser.page_source
			file_path = '{0}/{1}.{2}'.format('port_images', proxy, 'jpg')
			with open(file_path, 'wb') as f:
				f.write(port.encode())
		except TimeoutException:
			print('连接超时')

	def run(self):
		self.get_images()

zdaye_crawler = ZdayeCrawler()
zdaye_crawler.run()
