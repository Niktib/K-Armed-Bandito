import BanditArmClass as BAC
import RandomNumberGenerator as RNG

#BanditMaker class is a class to organize the creation of a list that is populated by BanditArm objects
#And contains the function to return the list of bandit arms
class BanditMaker:
	def __init__(self, k, Randomizer):
		self.simpleList = []
		for index in range(k):
			self.simpleList.append(BAC.BanditArm(Randomizer))
	def getBanditArms(self):
		return self.simpleList
