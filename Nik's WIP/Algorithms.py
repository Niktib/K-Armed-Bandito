import math

class lrp:
	def __init__(self, alpha=0.01, beta=0.01):
		self.alpha = alpha 
		self.beta = beta
		
	def updatingArray(self, arr, i, success):
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
		
	def updatingArray(self, arr, i, success):
		if (success == 0): return arr
		for index in range(len(arr)):
			if (index == i ):
				arr[index] = arr[index] + self.alpha * (1 - arr[index])
			else:
				arr[index] = (1-self.alpha)* arr[index]
		return arr