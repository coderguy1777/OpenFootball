import pandas as pd
import numpy as np
import cv2 as opencv
import DataFile
from sklearn import *
import matplotlib.pyplot as plt

class DataLoopTeamStats:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        self.xreshape = self.value1.reshape(len(value1), 1)
        self.yreshape = self.value2.reshape(len(value2), 1)
        self.teamdic = {}

    def fileloop(self, filename):
        df = pd.read_csv(filename + ".csv", index_col=False, header=0, names=['Wins', 'Losses', 'Ties', 'Super bowl Wins'])
        self.value1 = df['Wins'].values
        self.value2 = df['Losses'].values
        linreg = linear_model.LinearRegression()
        linregfit = linreg.fit(self.value1, self.value2)
        x_predictions = linreg.predict(self.value1)
        y_predictions = linreg.predict(self.value2)
        plt.scatter(self.value1, self.value2, color='red')
        plt.plot(self.value1, x_predictions, label='Best Fit Line', color='black')
        for teamval in DataFile.teamvalues:
            if teamval == filename:
                filename = teamval
                self.fileloop(teamval)

        for winlossval in df['Wins']:
            self.teamdic = {}
