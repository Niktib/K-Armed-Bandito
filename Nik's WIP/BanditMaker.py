import BanditArmClass as BAC

class BanditMaker:
	def __init__(self, k):
		self.simpleList = []
		for index in range(k):
			self.simpleList.append(BAC.BanditArm())
	def getBanditArms(self):
		return self.simpleList
