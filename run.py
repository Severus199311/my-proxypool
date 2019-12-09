import sys
import io
from proxypool.scheduler import Scheduler



def main():
	try:
		scheduler = Scheduler()
		scheduler.run()
	except:
		main()

if __name__ == '__main__':
	main()