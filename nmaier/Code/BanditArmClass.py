# Name, Student Number
# Nikolas Maier, 500461990
# Oluwatomilayo Adegbite, 500569283
class BanditArm:
	#When a bandit arm initializes it creates its own copy of the RNG object
	#It then generates it's unique probability for pulling the arm and generating a success
	def __init__(self, Probability):
		self.prob = Probability
		self.timesPulled = 0
		self.GoodPull = 0
		
	#The pull function generates a random number and checks if it is below the arm's success probability
	#On success return 1, on failure return 0
	def Pull(self, PuledNumber):
		self.timesPulled += 1
		if (PuledNumber < self.prob):
			self.GoodPull += 1
			return 1
		else:
			return 0
			
	def Average(self):
		return self.GoodPull /self.timesPulled
		
	#Stats returns the arms probability, this way we can check which has the highest probability or can compare and contrast information.
	def stats(self):
		return self.prob