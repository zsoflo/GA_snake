import random
import numpy as np
from typing import NewType, List

# UserID = int
# user = UserID(10)
# print(user)

UserID = NewType('UserID', int)
user = UserID(10)

def find_user(user_id: UserID):
    print('Found:', user_id)

find_user(10)
find_user(10)

def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))

class Network(object):

    def __init__(self, sizes):
        
        self.num_layers = len(sizes)
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y, in zip(sizes[:-1], sizes[1:])]
        
    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a