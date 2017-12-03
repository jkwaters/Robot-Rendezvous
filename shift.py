import random

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput
       break

def shift(position, distance, n):
    if (position + distance) <= 0: # (position + distance) result is negative and we 
        return (n + position + distance)
    if (position + distance) > n: # shift is greater than n (the number of nodes)
        return (n - position + distance)
    else:
        return (position + distance)

# test edge cases & basic sanity testing
# print(shift(1, -1, 10))
# print(shift(10, 1, 10))
# print(shift(1, 1, 10))
# print(shift(10, -1, 10))




iterations = 0
n = 1000 # inputNumber("How many nodes? ")
numRobots = 50 # inputNumber("How many robots? ")
robots = set(random.sample(range(1, n+1), numRobots))
print(robots)

while len(robots) > 1:
    iterations += 1
    lenBefore = len(robots)
    robotsBefore = set(robots)
    robotsAfter = set()
    moves = list()

    while len(robotsBefore) > 0:
        move = random.randint(1,int(n/lenBefore)) * random.choice([-1, 1])
        moves.append(move)
        robotsAfter.add(shift(robotsBefore.pop(),move,n))
        robotsAfter.difference_update(robotsBefore)
        # print(robotsBefore, robotsAfter)

    if len(robotsAfter) != lenBefore:
         print(robots)
         print(moves)
         print(robotsAfter, ' : ', len(robotsAfter), ' : ', iterations)
    robots = set(robotsAfter)

# print(robots, ' : ', iterations)