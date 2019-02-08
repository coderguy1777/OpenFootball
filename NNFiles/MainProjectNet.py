import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import *

df = pd.read_csv("Testdata.csv", encoding="latin-1", index_col=False, header=0, names=['Type1', 'Type2'])
x = df['Type1'].values
y = df['Type2'].values
regr = linear_model.LinearRegression()
x = x.reshape(len(x), 1)
y = y.reshape(len(y), 1)
regr.fit(x, y)
inputsaxisypred = regr.predict(x)
inputaxisarr = regr.predict(y)
plt.scatter(x, inputaxisarr, color='red')
plt.plot(x, inputsaxisypred, label='Best fit line', color='blue')
plt.xticks()
plt.yticks()
plt.legend()
plt.show()