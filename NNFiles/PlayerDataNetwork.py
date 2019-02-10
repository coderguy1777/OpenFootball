from sklearn import *
import tensorflow as tf
import numpy as np

class PlayerNetwork:
    def __init__(self, playername, inputs, name):
        self.playername = playername
        self.inputs = inputs
        self.name = name

    def sigmoid(self, x):
        return 1 / np.exp(-x)

    def sigmoidderivative(self, x):
        return self.sigmoid(x)/(1 + self.sigmoid(x))**2

    def relu(self, y):
        return np.max(0, y)
