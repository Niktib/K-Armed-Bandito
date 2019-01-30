import math

class UCB:
	def __init__(self, c=2):
		self.c = c
	#The below algorithm accepts various
	def Picker(self, TotalRunTime, PickedArr, ProbArr):
		GreatestAction = 0
		ActionToPick = 0
		for index in range(len(PickedArr)):
			CurrentAction = ProbArr[index] + self.c * math.sqrt(math.log10(TotalRunTime)/PickedArr[index])
			if (CurrentAction > GreatestAction):
				ActionToPick = index
		return ActionToPick

class SimpleUpdate:
	def Update(self, timesPicked, Reward, CurrentProbability):
		UpdatedValue = CurrentProbability + (1/timesPicked) * (Reward - CurrentProbability)
		return UpdatedValue
	
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