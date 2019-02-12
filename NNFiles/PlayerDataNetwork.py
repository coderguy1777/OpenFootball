from sklearn import *
import tensorflow as tf
import pandas as pd
import numpy as np

class PlayerNetwork:
    def __init__(self, playername, inputs, teamval):
        self.playername = playername
        self.dic = {}
        self.teamval = teamval
        self.inputs = inputs

    def sigmoid(self, x):
        return 1 / np.exp(-x)

    def sigmoidderivative(self, x):
        return self.sigmoid(x)/(1 + self.sigmoid(x))**2

    def relu(self, y):
        return np.max(0, y)


    def mainnet(self, teamvar):
        playerteammap = []
        for i in self.playername:
            for x in self.inputs:
                playerteammap.append(i)
                self.dic = {i: x}
                print(self.dic)

df = pd.read_csv('Testdata2.csv', encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])

teamplayers = []
for name in df['Name']:
    teamplayers.append(name)

teamvalue = "Seattle Seahawks"
clf = PlayerNetwork(df['Name'], df['Position'], teamvalue)
clf.mainnet(teamvalue)

