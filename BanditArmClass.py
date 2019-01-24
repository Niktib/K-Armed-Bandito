import RandomNumberGenerator as RNG
class BanditArm:
	def __init__(self):
		self.prob = RNG.RandomNumGen.RandomGen()
	def Pull(self):
		CurrentPull = RNG.RandomNumGen.RandomGen()
		if (CurrentPull < self.prob):
			return 1
		else:
			return 0
	def stats(self):
		return self.prob