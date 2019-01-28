class BanditArm:
	def __init__(self, Randomizer):
		self.prob = Randomizer
		self.timesPulled = 0
		self.GoodPull = 0
	def Pull(self, pullProb):
		CurrentPull = pullProb
		self.timesPulled += 1
		if (CurrentPull < self.prob):
			self.GoodPull += 1
			return 1
		else:
			return 0
	def stats(self):
		return self.prob, self.timesPulled
