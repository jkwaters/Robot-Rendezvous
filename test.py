import shift

tests = 100
bigSteps = False # ROBOTS move 1 hop per iteration

# FULL RING OF ROBOTS
# for nodes in (10 ** exponent for exponent in range(1,4)):
#     totalIterations = 0
#     totalShifts = 0
#     numRobots = int(nodes/2)
#     for i in range(0,tests):
#         result = shift.rendezvouz(nodes, numRobots, bigSteps, output=False)
#         totalIterations += result[0]
#         totalShifts += result[1]
#         # print(robots, ' : ', totalIterations)
#     avgIterations = totalIterations / tests
#     avgShifts = totalShifts / tests
#     print(nodes, avgIterations, avgShifts)


# 2 to 20 robots on 20 node ring
# nodes = 20
# for numRobots in range(2,nodes+1):
#     totalIterations = 0
#     totalShifts = 0
#     for i in range(0,tests):
#         result = shift.rendezvouz(nodes, numRobots, bigSteps, output=False)
#         totalIterations += result[0]
#         totalShifts += result[1]
#     avgIterations = totalIterations / tests
#     avgShifts = int(totalShifts / tests)
#     print (numRobots, avgIterations, avgShifts, sep=', ')

nodes = 200
for numRobots in range(2,nodes+1,5):
    totalIterations = 0
    totalShifts = 0
    for i in range(0,tests):
        result = shift.rendezvouz(nodes, numRobots, bigSteps, output=False)
        totalIterations += result[0]
        totalShifts += result[1]
    avgIterations = totalIterations / tests
    avgShifts = int(totalShifts / tests)
    print (numRobots, avgIterations, avgShifts, sep=', ') 









# nodes = 1000 # shift.inputNumber("How many nodes? ")
# # numRobots = 10 # shift.inputNumber("How many robots? ")
# # Ask movement specifics

# for numRobots in range(int(nodes/10),nodes+1,int(nodes/10)):
#     totalIterations = 0
#     totalShifts = 0
#     for i in range(0,tests):
#         result = shift.rendezvouz(nodes, numRobots)
#         totalIterations += result[0]
#         totalShifts += result[1]
#         # print(numRobots, ' : ', totalIterations)
#     avgIterations = totalIterations / tests
#     avgShifts = totalShifts / tests
#     print (numRobots, avgIterations, avgShifts) 