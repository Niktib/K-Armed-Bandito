import math

class UCB:
	def __init__(self, c=2):
		self.c = c
		
	def updateReward(self, totalTimes, num, reward, previousValue):
		updatedValue = previousValue + self.c * math.sqrt(math.log10(totalTimes)/num)
		return updatedValue
		
class lrp:
	def __init__(self, alpha=0.01, beta=0.01):
		self.alpha = alpha 
		self.beta = beta
		
	def updatingArray(self, arr, i, success):
		for index in range(len(arr)):
			if (index == i ):
				if (success == true):
					arr[index] = arr[index] + self.alpha * (1 - arr[index])
				else:
					arr[index] = (1-self.beta)* arr[index]
			else:
				if (success == true):
					arr[index] = (1-self.alpha)* arr[index]
				else:
					arr[index] = self.beta/(len(arr)-1) + (1-self.beta)*arr[index]
		return arr
		
class lri:
	def __init__(self, alpha=0.01):
		self.alpha = alpha 
		
	def updatingArray(self, arr, i, success):
		if (success == false) return arr
		for index in range(len(arr)):
			if (index == i ):
				arr[index] = arr[index] + self.alpha * (1 - arr[index])
			else:
				arr[index] = (1-self.alpha)* arr[index]
		return arr