import Robot

class Cycle:
    """Doubly linked list"""

    totalRobots = 0
    # nodes = 100

    def __init__(self, nodes=100, robots):
        self.nodes = nodes
        self.cycle = [None] * nodes
        self.startingRobots = robots
        # initialize robots in cycle


    def initRobots(self):
        