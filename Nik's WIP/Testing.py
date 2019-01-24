import BanditMaker as Bandit
import BanditArmClass as BAC
import RandomNumberGenerator as RNG

class TestBed:
	def __init__(self, n):
		self.n = n

class Gambler:
	def __init__(self, k):
		self.ProbArr = []
		self.RewardsArr = []
		self.BanditArmsArr = []
		self.BanditsPickedArr = []
		for index in range(k):
			self.ProbArr.append(1.0/k)
			self.RewardsArr.append(0)
			self.BanditsPickedArr.append(0)
		
test = Bandit.BanditMaker(4)

#test = BanditMaker(1)