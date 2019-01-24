import random
from datetime import datetime

class RandomNumGen:
	def RandomNumberGen():
		random.seed(datetime.now())
		return random.random()