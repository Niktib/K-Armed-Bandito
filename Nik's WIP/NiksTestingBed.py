import BanditMaker as Bandit
import BanditArmClass as BAC
import RandomNumberGenerator as RNG
import Algorithms as AG 
import os

class TestBed:
	def __init__(self, n, k, l):
		self.n = n #number of runs
		self.k = k #number of arms
		self.l = l #Number of interactions with the environment
		f = open(os.path.dirname(os.path.realpath(__file__)) + "\TestData.txt","w")
		f.write("Gambler #,Round #,Times optimal action picked,Average reward \n")
		for index in range(self.n):
			GamblerObject = Gambler(self.k, f, index)
			GamblerObject.StartPullingArms(self.l)
			
		f.close()

class Gambler:
	#The below initialization function sets up all the items needed for creating a K-Armed Bandit 
	def __init__(self, k, f, n):
		self.f = f #Text file log
		self.k = k
		self.n = n #Current iteration of the Gambler
		self.Randomizer = RNG.RandomNumGen
		self.ProbArr = []			#stores the probabilities of picking each arm 
		self.RewardsArr = []		#Stores the history of the rewards for each arm cumulatively
		self.BanditArmsArr = Bandit.BanditMaker(k, self.Randomizer).getBanditArms()		#Stores each bandit arm 
		self.BanditsPickedArr = []	#Stores how many of each has been picked
		#The below for loop fills in all the defaults
		#0's for all the counters of rewards and times picked and a probability divided equally amongst all arms for the Value 
		for index in range(k):
			self.ProbArr.append(1.0/self.k)
			self.RewardsArr.append(0)
			self.BanditsPickedArr.append(0)
		
	#StartPullingArms takes parameter l, which is the number of times the arms should be pulled.
	#It records the results in all of the arrays
	def StartPullingArms(self, l):
		self.Optimal = self.OptimalArm()
		UpdaterOfArray = AG.lrp()
		for index in range(l):
			if (index % 100 == 0): 
				self.LogResults(index)
			ArmPicked = self.RandomPickOfArms()
			Result = self.BanditArmsArr[ArmPicked].Pull()
			self.RewardsArr[ArmPicked] = self.RewardsArr[ArmPicked] + Result
			self.BanditsPickedArr[ArmPicked] += 1
			self.ProbArr = UpdaterOfArray.updatingArray(self.ProbArr, ArmPicked, Result)
			
		self.LogResults(l)

	def OptimalArm(self):
		i = 0
		k = -1
		for index in range(len(self.BanditArmsArr)):
			if (self.BanditArmsArr[index].stats() > i):
				k = index
				i = self.BanditArmsArr[index].stats()
		return k
		
	#This function just figures out which arm correlates with which randomly generated number 
	def RandomPickOfArms(self):
		WhichArm = self.Randomizer.RandomGen()
		i = 0
		for index in range(len(self.ProbArr)):
			i = i + self.ProbArr[index]
			if (WhichArm < i):
				return index 
				
	def LogResults(self, index):
		self.f.write(str(self.n) + "," + str(index) + "," + str(self.Optimal) + "," + str(self.AverageReward()) + "," + str(self.BanditsPickedArr[self.Optimal]) + "\n")
		
	def AverageReward(self):
		total = 0
		for index in range(len(self.RewardsArr)):
			total = total + self.RewardsArr[index]
		return total/self.k
		

#print(os.path.dirname(os.path.realpath(__file__)))	
test = TestBed(100, 10, 5000)
