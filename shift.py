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




iterations = 0
n = 10 # inputNumber("How many nodes? ")
numRobots = 5 # inputNumber("How many robots? ")
robots = set(random.sample(range(1, n+1), numRobots))
print(robots)

while len(robots) > 1:
    iterations += 1
    robotsBefore = robots
    robotsAfter = set()

    while len(robotsBefore) > 0:
        robotsAfter.add(shift(robotsBefore.pop(),1,n))
        robotsAfter.difference_update(robotsBefore)
        print(robotsBefore, robotsAfter)

    print(robotsAfter, ' : ', iterations)
    
    robots = robotsAfter
    if iterations >= 50:
        break
