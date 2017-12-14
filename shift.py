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

def yes_or_no(question):
    reply = str(input(question + ' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter a valid input")

def shift(position, distance, n):
    if (position + distance) <= 0: # (position + distance) result is negative and we 
        return (n + position + distance)
    if (position + distance) > n: # shift is greater than n (the number of nodes)
        return (n - position + distance)
    else:
        return (position + distance)



def rendezvouz(nodes, numRobots, bigSteps, output=False, verbose=False):
    iterations = 0
    shifts = 0
    robots = set(random.sample(range(1, nodes+1), numRobots))
    # print("robots: ", robots)

    while len(robots) > 1:
        iterations += 1
        lenBefore = len(robots)
        robotsBefore = set(robots)
        robotsAfter = set()
        moves = list()

        while len(robotsBefore) > 0:
            move = random.choice([-1, 1])
            if bigSteps:
                move = move * random.randint(1,int(nodes/lenBefore))
            moves.append(move)
            robotsAfter.add(shift(robotsBefore.pop(),move,nodes))
            shifts += 1
            robotsAfter.difference_update(robotsBefore)

        if output:
            if verbose:
                print("\nbefore: ", robots)
                print("move:   ", moves)
                print("after:  ", robotsAfter, ' : ', len(robotsAfter), ' : ', iterations)
            elif len(robotsAfter) != lenBefore:
                print("\nbefore: ", robots)
                print("move:   ", moves)
                print("after:  ", robotsAfter, ' : ', len(robotsAfter), ' : ', iterations)
            
        robots = set(robotsAfter)
    return (iterations, shifts)

# test edge cases & basic sanity testing
# print(shift(1, -1, 10))
# print(shift(10, 1, 10))
# print(shift(1, 1, 10))
# print(shift(10, -1, 10))