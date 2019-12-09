import time
from multiprocessing import Process
from proxypool.getter import Getter 
from proxypool.tester import Tester 
from proxypool.api import app
from settings import *
from proxypool.db import RedisClient

class Scheduler():
	def schedule_getter(self):
		getter = Getter()
		while True:
			print('获取器开始运行')
			getter.run()
			time.sleep(GETTER_CYCLE)

	def schedule_tester(self):
		tester = Tester()
		while True:
			print('检测器开始运行')
			tester.run()
			time.sleep(TESTER_CYCLE)

	def schedule_delete_all(self):
		redis = RedisClient()
		redis.delete_all()
		print('旧有代理已清除')

	def schedule_api(self):
		app.run(API_HOST, API_PORT)

	def run(self):
		print('代理池开始运行')
		if DELETE_ALL:
			delete_all_process = Process(target = self.schedule_delete_all)
			delete_all_process.start()

		if TESTER_ENABLED:
			tester_process = Process(target = self.schedule_tester)
			tester_process.start()

		if GETTER_ENABLED:
			getter_process = Process(target = self.schedule_getter)
			getter_process.start()

		if API_ENABLED:
			api_process = Process(target = self.schedule_api)
			api_process.start()

