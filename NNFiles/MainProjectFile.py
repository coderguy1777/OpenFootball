import matplotlib.pyplot as plt
import pandas as pd
from sklearn import *
from DataInputs import DataFileLoop

df = pd.read_csv("Testdata.csv", encoding="latin-1", index_col=False, header=0, names=['Type1', 'Type2'])
x = df['Type1'].values
y = df['Type2'].values
regr = linear_model.LinearRegression()
x = x.reshape(len(x), 1)
y = y.reshape(len(y), 1)
regr.fit(x, y)
inputsaxisypred = regr.predict(x)
plt.scatter(x, y, color='red')
plt.plot(x, regr.predict(x), label='test', color='blue')
plt.show()
filelooper = DataFileLoop.DataLoop()

filenamelist = []
filenamelist.append('NetworkData/output-onlinerandomtools.csv')
filenamelist.append('NetworkData/testfile.csv')

for fileval in filenamelist:
    filelooper.fileloop(fileval)