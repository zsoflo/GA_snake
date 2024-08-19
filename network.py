import random
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

class network(object):

    food_pos = []

    segments = []

    def __init__(self):
        
        print("sss...")

        self.sizes = [3, 10, 4]
        self.num_layers = len(self.sizes)
        self.biases = [np.random.randn(y, 1) for y in self.sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y, in zip(self.sizes[:-1], self.sizes[1:])]
        
    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        return a

    def move(self, food_pos, segments):
        self.food_pos = food_pos
        self.segments = segments

        return random.choice([0, 1, 2, 3])