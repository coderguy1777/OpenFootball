import numpy as np
from sklearn import *
import matplotlib.pyplot as plt
import pandas as pd

class LinearReg:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def linregmethod(self, file, predx, predy):
        df = pd.read_csv(file, encoding="latin-1", index_col=False, header=0, names=['Type1', 'Type2'])
        x = df['Type1'].values
        y = df['Type2'].values
        regr = linear_model.LinearRegression()
        x = x.reshape(len(x), 1)
        y = y.reshape(len(y), 1)
        regr.fit(x, y)
        inputsaxisypred = regr.predict(x)
        plt.scatter(x, y, color='red')
        plt.plot(x, inputsaxisypred, label='test', color='blue')
        plt.show()