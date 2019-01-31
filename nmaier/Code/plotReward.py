# Name, Student Number
# Nikolas Maier, 500461990
# Oluwatomilayo Adegbite, 500569283
import matplotlib.pyplot as plt

class plotReward:
	def __init__(self,name):
		self.name = name
		self.logList = list()
		self.ProbGraph = plt

	def LogResults(self,AverageReward):
		self.logList.append(AverageReward)
		pass
	def LogProb(self, Probability):
		self.ProbGraph.plot(Probability, label='Chance of Picking Optimal Arm')

	def plotProb(self, WhichAlgorithm):
		if (WhichAlgorithm == 1): self.name = "UCB"
		elif (WhichAlgorithm == 2): self.name = "LRI"
		elif (WhichAlgorithm == 3): self.name = "LRP"
		#plt.plot(self.logList,label='Chance of Picking Optimal Arm')
		self.ProbGraph.xlabel('Steps')
		self.ProbGraph.ylabel('Probability')
		self.ProbGraph.title('Probability over 20 Runs')
		self.ProbGraph.grid(True)
		self.ProbGraph.savefig('GraphOf{}.png'.format(self.name))
		self.ProbGraph.clf() #clear the current graph, can be removed to see all values on one chart
		
	def plotUCB(self):
		self.name = "UCB"
		#plt.plot(self.logList,label='Chance of Picking Optimal Arm')
		self.ProbGraph.xlabel('Steps')
		self.ProbGraph.ylabel('Average Reward')
		self.ProbGraph.title('Average Reward over 20 Runs')
		self.ProbGraph.grid(True)
		self.ProbGraph.savefig('GraphOf{}.png'.format(self.name))
		self.ProbGraph.clf() #clear the current graph, can be removed to see all values on one chart
		
	def plot(self):
		plt.plot(self.logList,label=self.name)
		plt.xlabel('Steps')
		plt.ylabel('Average Rewards')
		plt.title('Average Reward for {}'.format(self.name))
		plt.grid(True)
		plt.savefig('GraphOf{}.png'.format(self.name))
		plt.clf() #clear the current graph, can be removed to see all values on one chart
