import BanditArmClass as BAC
import random
from datetime import datetime
import Algorithms as AG 
import plotReward
import os

class TestBed:
	def __init__(self, n=100, k=10, l=5000, WhichAlgorithm=1):
		#WhichAlgorithm will be a number between 1 and 3 to clarify which style of algorithm will be applied to the running of the Gambler.
		#1 is UCB, 2 is Learning Reward-Inaction, 3 is Learning Reward-Penalty
		#n is number of runs
		#k is number of arms
		#l is Number of times the arms should be pulled
		if (WhichAlgorithm == 1): AlgorithmName = "UCB"
		elif (WhichAlgorithm == 2): AlgorithmName = "LRI"
		elif (WhichAlgorithm == 3): AlgorithmName = "LRP"
		graphMaker = plotReward.plotReward("test")
		f = open(os.path.dirname(os.path.realpath(__file__)) + "\TestData{}.txt".format(AlgorithmName),"w")
		f.write("Gambler #,Round #,OptimalArm,Average reward, Times optimal action picked,Probability of Picking Optimal\n")
		for index in range(n):
			GamblerObject = Gambler(k, f, index, WhichAlgorithm)
			test =(GamblerObject.StartPullingArms(l))
			graphMaker.LogProb(test)
		
		
		graphMaker.plotProb(WhichAlgorithm)
		f.close()

class Gambler:
	#The below initialization function sets up all the items needed for creating a K-Armed Bandit 
	def __init__(self, k, outfile, n, WhichAlgorithm):
		self.outfile = outfile #Text file log
		self.k = k #Number of arms
		self.n = n #Current iteration of the Gambler
		random.seed(datetime.now())
		self.BanditArmsArr = []
		self.ProbArr = []			#stores the probabilities of picking each arm cumulatively
		self.WhichAlgorithm = WhichAlgorithm		
		
		#The below for loop fills in all the defaults
		#0's for all the counters of rewards and times picked and a probability divided equally amongst all arms for the Value 
		self.choosePolicy()
		for index in range(self.k):
			self.BanditArmsArr.append(BAC.BanditArm(random.random()))
		self.Optimal = self.OptimalArm()
			
	#The ChooseMethod method helps decide which policy will be used: UCB, LRI or LRP
	def choosePolicy(self):
		if (self.WhichAlgorithm == 1):
			self.Policy = AG.UCB()			
		elif (self.WhichAlgorithm == 2):
			self.Policy = AG.lri()
		else:
			self.Policy = AG.lrp()
			
		for index in range(self.k):
			if (self.WhichAlgorithm == 1):
				self.ProbArr.append(0)
			else:
				self.ProbArr.append(1.0/self.k) #For LRI or LRP style choosing

		
	#StartPullingArms takes parameter l, which is the number of times the arms should be pulled.
	#It records the results in the arrays
	def StartPullingArms(self, l):
		#The below object should be changeable depending on if we are doing UCB, Greedy, LRP or LRI
		PlottingList = []
		self.iteration = 0
		for index in range(l):
			if (index % 100 == 0): 
				self.LogResults(index)
				PlottingList.append(self.ProbArr[self.Optimal])
			self.iteration = index
			self.ArmPicked = self.Policy.action(self)
			self.Result = self.BanditArmsArr[self.ArmPicked].Pull(random.random())
			#If LRI or LRP it will update the probability arrays
			if (self.WhichAlgorithm > 1):
				self.ProbArr = self.Policy.updatingArray(self)
				
		self.LogResults(l)
		return PlottingList

	def OptimalArm(self):
		i = 0
		k = -1
		for index in range(len(self.BanditArmsArr)):
			if (self.BanditArmsArr[index].prob > i):
				k = index
				i = self.BanditArmsArr[index].prob
		return k
						
	def LogResults(self, index):
		self.outfile.write(str(self.n) + "," + str(index) + "," + str(self.Optimal) + "," + str(self.AverageReward()) + "," + str(self.BanditArmsArr[self.Optimal].timesPulled) + "," + str(self.ProbArr[self.Optimal]) + "," + str(self.BanditArmsArr[self.Optimal].prob) + "\n")
		
	def AverageReward(self):
		total = 0
		for index in range(len(self.BanditArmsArr)):
			total = total + self.BanditArmsArr[index].GoodPull
		return total/self.k

