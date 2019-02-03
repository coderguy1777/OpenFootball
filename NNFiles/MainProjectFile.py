import tensorflow as tf
import cv2 as opencv
import numpy as np
from NNFiles.LinearRegression import LinearRegression

data1 = []
data2 = []
for i in range(7):
    data1.append(np.random.randint(0, 10, size=9))
for i2 in range(7):
    data2.append(np.random.randn(20))


clf = LinearRegression(data1, data2)
clf.b1val()
clf.b1finaleq()
clf.b0val()
clf.linearregressioneq()
for i in data1:
    clf.yhat(i)
    clf.dataplot(clf.yhat(i), i)

