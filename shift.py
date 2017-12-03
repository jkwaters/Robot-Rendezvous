import random

def shift(x, k, n):
    k = random.choice([-1, 1]) * k
    if (x + k) <= 0: # (x + k) result is negative and we 
        return (n + x + k)
    if (x + k) > n: # shift is greater than n (the number of nodes)
        return (n - x + k)
    else:
        return (x + k)

# test edge cases & basic sanity testing
# print(shift(1, -1, 10))
# print(shift(10, 1, 10))
# print(shift(1, 1, 10))
# print(shift(10, -1, 10))


iterations = 0
n = 13
numRobots = 12
robots = set(random.sample(range(1, n+1), numRobots))
print(robots)

while len(robots) > 1:
    iterations += 1
    robots = set([shift(x,1,n) for x in robots])
    print(robots, ' : ', iterations)
