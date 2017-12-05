import shift

tests = 1000
nodes = 10 # shift.inputNumber("How many nodes? ")
# numRobots = 10 # shift.inputNumber("How many robots? ")
# Ask movement specifics

for numRobots in range(int(nodes/10),nodes+1,int(nodes/10)):
    totalIterations = 0
    totalShifts = 0
    for i in range(0,tests):
        result = shift.rendezvouz(nodes, numRobots)
        totalIterations += result[0]
        totalShifts += result[1]
        # print(robots, ' : ', totalIterations)
    avgIterations = totalIterations / tests
    avgShifts = totalShifts / tests
    print (numRobots, avgIterations, avgShifts)