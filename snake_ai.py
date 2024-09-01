import random
from network import Network

class snake(object):

    food_pos = []

    segments = []

    moves = []

    def __init__(self):
        print("ssss")
        self.network_architecture = Network([2, 4])

        self.fitness = 100

        # self.network.str()

    def move(self, food_pos, segments):

        self.fitness -= 1

        #self.food_pos = food_pos
        #self.segments = segments
        #self.direction = self.network_architecture.feedforward()

        return random.choice([0, 1, 2, 3])

        return self.direction

    def reward(self):

        self.fitness += 100
    
    def reset(self):

        self.__init__()

zso = snake()
zso.network_architecture.str()
