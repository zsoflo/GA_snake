import random
import numpy as np

def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))

class Network(object):

    def __init__(self, sizes):
        
        self.num_layers = len(sizes)
        firstlayerbiases = [np.zeros(sizes[(0)], dtype = float)]
        self.biases = firstlayerbiases + [np.random.randn(y) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y, in zip(sizes[:-1], sizes[1:])]
        
    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a
    
    def str(self):

        for layer in range(self.num_layers):
            print("This is layer " + str(layer + 1) +"!")
            print(self.biases[layer])

        # # print(self.biases)
        # for layer in self.biases:
        #     print("This is a layer, biases: " + str(layer))
        #     for neuron in layer:
        #         print("This is a neuron's bias: " + str(neuron))
        #         for layer in self.weights:
        #             for neuron in layer:
        #                 print("This is a neuron's weights:" + str(neuron))

        # # print(self.weights)
        # for layer in self.weights:
        #     print("This is a layer, weights" + str(layer))
        #     for neuron in layer:
        #         print("This is a neuron's weights:" + str(neuron))

network1_test = Network([4, 4, 4, 4])
# network1_test.str()
