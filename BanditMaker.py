import BanditArmClass as BAC
import RandomNumberGenerator as RNG
class BanditMaker:
	def __init__(self, k, Randomizer):
		self.simpleList = []
		for index in range(k):
			self.simpleList.append(BAC.BanditArm(Randomizer))
	def getBanditArms(self):
		return self.simpleList
