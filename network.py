import random
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

class Network(object):

    def __init__(self, sizes):
        
        self.num_layers = len(sizes)
        self.sizes = sizes
        firstlayer = [np.zeros(sizes[(0)], dtype = float)]
        self.biases  = firstlayer + [np.random.randn(y) for y in sizes[1:]]
        self.weights = firstlayer + [np.random.randn(y, x) for x, y, in zip(self.sizes[:-1], self.sizes[1:])]
        
    def feedforward(self, food, head):
        self.weights[0][np.array(food.x, food.y, head.x, head.y)]
        print(a)
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        print(a)
        return a
    
    def str(self):

        for layer in range(self.num_layers):
            print("This is layer " + str(layer + 1) +"!")
            print(self.biases[layer])

# network1_test = Network([4, 4, 4, 4])
# network1_test.str()