import math
import random

class UCB:
	def __init__(self, c=4):
		self.c = c
	def action(self, TestBed):
		actionArry = [None] * len(TestBed.BanditArmsArr)
		for i in range(len(TestBed.BanditArmsArr)):
			if (TestBed.BanditArmsArr[i].timesPulled > 0):
				actionArry[i] = TestBed.BanditArmsArr[i].Average() + self.c * math.sqrt( (math.log(TestBed.iteration)) / TestBed.BanditArmsArr[i].timesPulled )
			else:
				actionArry[i] = 1
		action = actionArry.index(max(actionArry))

		return action

	def updateQ(self, TestBed, index):
		return TestBed.ProbArr[index] + (1/TestBed.iteration) * (TestBed.AverageRewardArm(index) - TestBed.ProbArr[index])

class lrp:
	def __init__(self, alpha=0.01, beta=0.01):
		self.alpha = alpha
		self.beta = beta

	#This function just figures out which arm correlates with which randomly generated number
	def action(self, testbed):
		WhichArm = random.random()
		i = 0
		for index in range(len(testbed.ProbArr)):
			i = i + testbed.ProbArr[index]
			if (WhichArm < i):
				return index

	def updatingArray(self, testbed):
		success = testbed.Result
		i = testbed.ArmPicked
		arr = testbed.ProbArr
		for index in range(len(arr)):
			if (index == i ):
				if (success == 1):
					arr[index] = arr[index] + self.alpha * (1 - arr[index])
				else:
					arr[index] = (1-self.beta)* arr[index]
			else:
				if (success == 1):
					arr[index] = (1-self.alpha)* arr[index]
				else:
					arr[index] = self.beta/(len(arr)-1) + (1-self.beta)*arr[index]
		return arr

class lri:
	def __init__(self, alpha=0.01):
		self.alpha = alpha

	#This function just figures out which arm correlates with which randomly generated number
	def action(self, testbed):
		WhichArm = random.random()
		i = 0
		for index in range(len(testbed.ProbArr)):
			i = i + testbed.ProbArr[index]
			if (WhichArm < i):
				return index

	def updatingArray(self, testbed):
		success = testbed.Result
		i = testbed.ArmPicked
		arr = testbed.ProbArr
		if (success == 0): return arr
		for index in range(len(arr)):
			if (index == i ):
				arr[index] = arr[index] + self.alpha * (1 - arr[index])
			else:
				arr[index] = (1-self.alpha)* arr[index]
		return arr
