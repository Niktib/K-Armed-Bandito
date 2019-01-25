import RandomNumberGenerator as RNG
class BanditArm:
	def __init__(self, Randomizer):
		self.Randomizer = Randomizer
		self.prob = self.Randomizer.RandomGen()
	def Pull(self):
		CurrentPull = self.Randomizer.RandomGen()
		if (CurrentPull < self.prob):
			return 1
		else:
			return 0
	def stats(self):
		return self.prob