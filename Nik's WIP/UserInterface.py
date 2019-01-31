import UnifiedTestBed as UTB
'''
print("Let's run some K-Armed Bandits \n")
print("First let's get some parameters \n")
print("The defaults are 100 iterations of 5000 pulls of a 10-Armed Bandit using UCB\n")
k = input("How many arms? :")
l = input("\nHow many times should it pull arms? :")
n = input("\nHow many iterations? :")
print("\nWhich algorithm? (1 = UCB, 2 = LRI, 3 = LRP )")
Algorithm = input(":")
test = UTB.TestBed(int(n), int(k), int(l), int(Algorithm))
'''

test = UTB.TestBed(100, 10, 5000, 1)
test = UTB.TestBed(100, 10, 5000, 2)
test = UTB.TestBed(100, 10, 5000, 3)
print("\nAll done, the test file and graphs should be in your folder\n")
