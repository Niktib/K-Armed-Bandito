import math

class UCB:
    def __init__(self):
        print("UCB Init")  # debug
        pass

    def action(self, armArry,Qarray, iteration, c=0.1):

        actionArry = [None] * len(armArry)
        for i in range( len(armArry) ):
            actionArry[i] = Qarray[i] + c * math.sqrt((math.log(iteration)) / armArry[i].timesPulled)
        action = actionArry.index(max(actionArry))
        print("actionArry: {}, armSelected: {}".format(actionArry,action))  # debug
        pass

    def updateQ(Qarray, index, alpha=0.1, rewardArr):
        Qarray[index] = Qarray[index] + alpha * (rewardArr[index] - )
        return Qarray
