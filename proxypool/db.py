from settings import *
import redis
from random import choice
import re
from proxypool.errors import PoolEmptyError

class RedisClient(object):
	def __init__(self, host = REDIS_HOST, port = REDIS_PORT, password = REDIS_PASSWORD):
		self.db = redis.StrictRedis(host = host, port = port, password = password, decode_responses = True)

	def add(self, proxy, score = INIT_SCORE):
		if not re.match('\d+\.\d+\.\d+\.\d+:\d+', proxy):
			print('代理', proxy, '不符合格式规范')
		elif not self.db.zscore(REDIS_KEY, proxy):
			return self.db.zadd(REDIS_KEY, {proxy: score})

	def random(self):
		result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
		if len(result):
			return choice(result)
		else:
			result = self.db.zrevrange(REDIS_KEY, 0, 100)
			if len(result):
				return choice(result)
			else:
				raise PoolEmptyError

	def decrease(self, proxy):
		score = self.db.zscore(REDIS_KEY, proxy)
		if score > MIN_SCORE:
			print('代理', proxy, '当前分数', score, '减一分')
			return self.db.zincrby(REDIS_KEY, -1, proxy)
		else:
			print('代理', proxy, '分数减完被删除')
			return self.db.zrem(REDIS_KEY, proxy)

	def exists(self, proxy):
		return not self.db.zscore(REDIS_KEY, proxy) == None

	def max(self, proxy):
		print('代理', proxy, '可用，分数设置为', MAX_SCORE)
		return self.db.zadd(REDIS_KEY, {proxy: MAX_SCORE})

	def count(self):
		return self.db.zcard(REDIS_KEY)

	def all(self):
		return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)

	def delete_all(self):
		return self.db.zremrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)




