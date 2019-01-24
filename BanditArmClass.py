import random


class BanditArm:
	def __init__(self):
		self.RNG = RandomNumGen()
		self.prob = self.RNG.RandomNumberGen()
	def Pull(self):
		CurrentPull = self.RNG.RandomNumGen()
		if (self.CurrentPull < self.prob):
			return 1
		else:
			return 0
	def stats(self):
		return self.prob