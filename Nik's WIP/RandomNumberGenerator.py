import random
from datetime import datetime

class RandomNumGen:
	def __init__(self):
		random.seed(datetime.now())
	def RandomGen():
		return random.random()