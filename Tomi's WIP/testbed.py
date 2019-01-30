import BanditArmClass as BAC
import UCBalgo
import random
import plotReward
from datetime import datetime


class TestBed:
	def __init__(self, numOfArms, name):
		self.k = numOfArms   # number of arms
		self.name = name

	def runIterations(self, numOfRuns, numberOfIteration,createGraph=True):
		self.n = numOfRuns  # number of runs
		f = open("TestData.txt", "w")
		f.write("Iteration #, Run #, Times optimal action picked, Average reward \n")
		UCBPolciy = UCBalgo.UCB()
		for iteration in range(1, numberOfIteration+1):
			graphMaker = plotReward.plotReward("{}, iter {}".format(self.name,iteration))
			SBArun = SBA(self.k, f, UCBPolciy)
			f.write("\n")
			for index in range(1, self.n+1):
				print("Iteration: {}, Run: {}".format(iteration, index))  # debug
				SBArun.StartPullingArms()
				SBArun.LogResults(index, iteration)
				graphMaker.LogResults(SBArun.AverageRewardIteration())
				if (index % 100 == 0):
					print("Index: {}, index % 100: {}".format(index, index % 100))
					SBArun.LogResults100(index, iteration)
			SBArun.printArmData()  # debug
			graphMaker.plot()
		f.close()


class SBA:   # Simple Bandit Algorithm
	#The below initialization function sets up all the items needed for creating a K-Armed Bandit
	def __init__(self, arms, outFile, Algorithm):
		print("SBA INIT")  # debug
		self.outFile = outFile   # Output file
		self.arms = arms
		random.seed(datetime.now())
		self.ProbArr = []			# stores the probabilities of picking each arm
		self.RewardsArr = []		# Stores the history of the rewards for each arm cumulatively
		self.BanditArmsArr = list()
		self.iteration = 1
		self.ArmPickedThisRound = -1  # debug
		self.Policy = Algorithm
		#The below for loop fills in all the defaults
		#0's for all the counters of rewards and times picked and a probability divided equally amongst all arms for the Value
		for index in range(arms):
			self.BanditArmsArr.append(BAC.BanditArm(random.random()))
			self.ProbArr.append(1.0/self.arms)
			self.RewardsArr.append(0)
		for i in self.BanditArmsArr:
			print("BanditArmsArr: {}".format(i.stats())) #debug
		print("Probability Array: {}".format(self.ProbArr)) #debug
		print("RewardsArr Array: {}".format(self.RewardsArr)) #debug
		#print("{} Arms \nRun Number: {}".format(self.arms, self.runNum))


	#StartPullingArms takes parameter l, which is the number of times the arms should be pulled.
	#It records the results in all of the arrays
	def StartPullingArms(self):
		print("Start Pulling Arms".format())
		self.Optimal = self.OptimalArm()
		ArmPicked = self.Policy.action(self)
		#ArmPicked = self.RandomPickOfArms()
		Result = self.BanditArmsArr[ArmPicked].Pull(random.random())
		self.RewardsArr[ArmPicked] = self.RewardsArr[ArmPicked] + Result
		print("Awards Array: {}".format(self.RewardsArr)) #debug
		print("Probability Array: {}".format(self.ProbArr)) #debug
		print("SBA Iteration: {}".format(self.iteration))
		#self.ProbArr = 	0
		#print("{} Arms \nRun Number: {}".format(self.arms, self.runNum))
		self.ArmPickedThisRound = ArmPicked
		self.iteration += 1
		'''
		for i in range(len(self.ProbArr)):
			self.ProbArr[i] = self.Policy.updateQ(self,i)
		'''

	def OptimalArm(self):
		i = 0
		k = -1
		print("OptimalArm Start") #debug
		for index in range(len(self.BanditArmsArr)):
			prob, timesPulled = self.BanditArmsArr[index].stats()
			if (prob > i):
				k = index
				i,timesPulled = self.BanditArmsArr[index].stats()
				print("Index: {} , timesPulled: {}".format(index,timesPulled))
		print("Arm Selected: {}".format(k))
		return k

	#This function just figures out which arm correlates with which randomly generated number
	def RandomPickOfArms(self):
		print("Picking Random") #debug
		WhichArm = random.random()
		i = 0
		for index in range(len(self.ProbArr)):
			i = i + self.ProbArr[index]
			if (WhichArm < i):
				return index

	def LogResults(self, index, Iteration):
		print("Log") #debug
		self.outFile.write("Arm Picked: {} ".format(self.ArmPickedThisRound))
		self.outFile.write("Iteration: {}, Run: {}, Optimal: {}, AverageReward: {}, TimesOptionalArmSelected, {} \n".format(Iteration, index, self.Optimal, self.AverageReward(), str(self.BanditArmsArr[self.Optimal].timesPulled)))

	def LogResults100(self, index, Iteration):
		print("Log100") #debug
		self.outFile.write("\nLog100: Iteration: {}, Run: {}, Optimal: {}, AverageReward: {}, TimesOptionalArmSelected, {} \n".format(Iteration, index, self.Optimal, self.AverageReward(), str(self.BanditArmsArr[self.Optimal].timesPulled)))

	def AverageReward(self):
		print("Average Reward") #debug
		total = 0
		for index in range(len(self.RewardsArr)):
			total = total + self.RewardsArr[index]
		return total/self.arms

	def AverageRewardIteration(self):
		print("Average Reward") #debug
		total = 0
		for index in range(len(self.RewardsArr)):
			total = total + self.RewardsArr[index]
		return total/self.iteration

	def AverageRewardArm(self, index):
		print("Average Reward Arm") #debug
		if self.BanditArmsArr[index].timesPulled > 0:
			return self.BanditArmsArr[index].GoodPull / self.BanditArmsArr[index].timesPulled
		else:
			return 0

	def printArmData(self): #debug mainly
		for i in range(len(self.BanditArmsArr)):
			arm = self.BanditArmsArr[i]
			self.outFile.write("Arm Index: {}, Arm Probability: {}, TimesPicked: {}, GoodPulls: {} \n".format(i,arm.prob, arm.timesPulled, arm.GoodPull))
		self.outFile.write("Probability Array: {} \nRewardsArray: {}\n".format(self.ProbArr, self.RewardsArr))


#print(os.path.dirname(os.path.realpath(__file__)))
test = TestBed(10, "10 Arms UCB")
test.runIterations(5000, 2)
