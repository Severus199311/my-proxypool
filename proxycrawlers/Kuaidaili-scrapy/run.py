from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from Kuaidaili.spiders.kuaidaili import KuaidailiSpider

def run():
	settings = dict(get_project_settings())
	process = CrawlerProcess(settings)
	process.crawl(KuaidailiSpider)
	process.start()

if __name__ == '__main__':
	run()