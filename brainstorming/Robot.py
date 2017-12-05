import random as r

class Robot:
    'Common base class for all employees'
    totalRobots = 0

    def __init__(self, position, movement=1, direction=1):
        self.position = position    # zero to n
        self.movement = movement    # how far 
        self.direction = direction  # either +1 or -1
        Robot.totalRobots += 1
    
    def displayCount(self):
        print "Total Robots %d" % Robot.totalRobots

    def setDirection(self):
        self.direction = r.choice([1,-1])

    def move(self):
        self.position = (self.position + self.direction)

    def merge(self):
        self.position