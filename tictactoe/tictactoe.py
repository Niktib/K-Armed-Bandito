class tictactoe:

# 1 will rep X

# 0 will rep O


    def __init__(self):
      self.board = [[None]*3,[None]*3,[None]*3]

    def victoryCheck(self):
      pass

    def boardState(self):
        emptyArray = list()
        xArrys = list()
        oArray = list()
        for i in range(3):
            for y in range(3):
                if self.board[i][y] is None:
                    emptyArray.append((i, y))
                if self.board[i][y] == 1:
                    xArrys.append((i, y))
                if self.board[i][y] == 0:
                    oArray.append((i, y))

        return emptyArray, xArrys, oArray


tic = tictactoe()  #debug
print(tic.board) #debug
tic.board[0][0] = 1 #debug
tic.board[0][1] = 1 #debug
tic.board[0][2] = 1 #debug
eA,xA,oA = tic.boardState() #debug
print("Empty Spots: {},\nX Spots:{},\nY Spots: {}".format(eA,xA,oA)) #debug
