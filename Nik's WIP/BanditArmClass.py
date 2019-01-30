import RandomNumberGenerator as RNG

class BanditArm:
	#When a bandit arm initializes it creates its own copy of the RNG object
	#It then generates it's unique probability for pulling the arm and generating a success
	def __init__(self, Randomizer):
		self.Randomizer = Randomizer
		self.prob = self.Randomizer.RandomGen()
	#The pull function generates a random number and checks if it is below the arm's success probability
	#On success return 1, on failure return 0
	def Pull(self):
		CurrentPull = self.Randomizer.RandomGen()
		if (CurrentPull < self.prob):
			return 1
		else:
			return 0
	#Stats returns the arms probability, this way we can check which has the highest probability or can compare and contrast information.
	def stats(self):
		return self.prob