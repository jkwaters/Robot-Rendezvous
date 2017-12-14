import shift

nodes = shift.inputNumber("How many nodes? ")
numRobots = shift.inputNumber("How many robots? ")
bigSteps = shift.yes_or_no("Can the robots take bigger steps?")
verbose = shift.yes_or_no("verbose output?")

result = shift.rendezvouz(nodes, numRobots, bigSteps, output=True, verbose=verbose)
iterations = result[0]
shifts = result[1]

print ("\n\n\ntotal iterations: ", iterations, "    total moves: ", shifts) 
