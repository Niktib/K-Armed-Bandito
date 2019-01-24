import random
from datetime import datetime

class RandomNumGen:
	def RandomGen():
		random.seed(datetime.now())
		return random.random()