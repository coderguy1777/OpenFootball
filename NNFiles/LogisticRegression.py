import numpy as np
import matplotlib as plt
import math

class LogisticRegression:
    def __init__(self, dataset1):
        self.dataset1 = dataset1
        self.valdict = {}

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoidderivative(self, x):
        return self.sigmoid(x)/(self.sigmoid(x) + 1)**2

    def lgreg(self):
        i = 0
        return i