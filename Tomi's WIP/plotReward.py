import matplotlib.pyplot as plt

class plotReward:
    def __init__(self,name):
        self.name = name
        self.logList = list()

    def LogResults(self,AverageReward):
        self.logList.append(AverageReward)
        pass

    def plot(self):
        plt.plot(self.logList,label=self.name)
        plt.xlabel('Steps')
        plt.ylabel('Average Rewards')
        plt.title('Average Reward for {}'.format(self.name))
        plt.grid(True)
        plt.savefig('GraphOf{}.png'.format(self.name))
        plt.clf() #clear the current graph, can be removed to see all values on one chart
