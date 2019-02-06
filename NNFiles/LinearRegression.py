import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self, data, data2):
        self.data = data
        self.data2 = data2
        self.linregdic = {}
        self.xsquaretot = 0
        self.ysquaretot = 0
        self.xmeanval = 0
        self.ymeanval = 0
        self.xysum = 0
        self.b1value = 0
        self.xsum = 0
        self.ysum = 0
        self.b0value = 0

    def b1val(self):
        self.xsum = np.sum(self.data)
        self.ysum = np.sum(self.data2)
        self.xmeanval = self.xsum / len(self.data)
        self.ymeanval = self.ysum / len(self.data2)
        xsum = np.sum(self.xsum - self.xmeanval)
        ysum = np.sum(self.ysum - self.ymeanval)
        self.xysum = np.sum(xsum* ysum)
        self.xsquaretot = np.sum(self.xsum - self.xmeanval)**2
        b1 = self.xysum / self.xsquaretot
        self.b1value = b1

    def b1finaleq(self):
        npoints = len(self.data) + len(self.data2)
        part1ofeq = self.xsum * self.ysum / npoints
        half1ofeq = self.xysum - part1ofeq
        part2ofeq = self.xsum ** 2 / npoints
        half2ofeq = self.xsquaretot - part2ofeq
        finaleq = half1ofeq/half2ofeq
        self.b1value = finaleq

    def b0val(self):
        npoints = len(self.data) + len(self.data2)
        tophalf = self.ysum - (self.b1value * self.xsum)
        bottomhalf = npoints
        finaleq = tophalf/bottomhalf
        self.b0value = finaleq
        return self.b0value

    def yhat(self, x):
        eq = self.b0value + self.b1value * x
        plt.plot(eq, x, 'ro', label="Predictions")
        plt.plot(eq, x)
        plt.legend()
        plt.show()
        return eq

    def linearregressioneq(self):
        print("y= " + str(self.b0value) + " + " + str(self.b1value) + "x")

    def dataplot(self, dataset, dataset2):
        plt.plot(dataset, dataset2, 'ro')
        plt.ylabel("Y Data")
        plt.xlabel("X Data")
        plt.show()