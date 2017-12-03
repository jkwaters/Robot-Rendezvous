import random

def shift(position, distance, n):
    distance = random.choice([-1, 1]) * distance
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

iterations = 0
n = 10 # inputNumber("How many nodes? ")
numRobots = 3 # inputNumber("How many robots? ")
robots = set(random.sample(range(1, n+1), numRobots))
print(robots)

while len(robots) > 1:
    iterations += 1
    robotsBefore = robots
    robotsAfter = set()

    while len(robotsBefore) > 1 or not robots.issubset(robotsAfter):
        robotsAfter.add(shift(robotsBefore.pop(),1,n))
        robotsAfter.difference_update(robotsBefore)
        print(robotsBefore, robotsAfter)

    print(robotsAfter, ' : ', iterations)
    
    robots = robotsAfter
    # robotsAftered = robotsAftered.difference(robotsAftered.intersection(robots)) # doesn't work with 3 numbers shifting, need to find a pair within +/- 1
    if iterations >= 50:
        break

# robotsAfter = set()
# while len(robots) > 1 and not robots.issubset(robotsAfter):
#     robotsAfter.add(shift(robots.pop(),1,n))
#     print(robots, robotsAfter)
