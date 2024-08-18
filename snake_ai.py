import random

class snake(object):

    food_pos = []

    segments = []

    moves = []

    def __init__(self):
        print("ssss")

    def move(self, food_pos, segments):
        self.food_pos = food_pos
        self.segments = segments

        return random.choice([0, 1, 2, 3])

    
