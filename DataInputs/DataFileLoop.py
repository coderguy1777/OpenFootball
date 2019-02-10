import pandas as pd
from sklearn import *
import tensorflow as tf
import numpy as np


class DataLoop:
    def __init__(self):
        self.filelist = []
        self.playerlist = {}
        self.teamlist = {}

    def fileloop(self, file):
        df = pd.read_csv(f"{file}", encoding="latin-1", names=['Wins', 'Losses', 'Win Percentage'])
        self.filelist.append(file)
        winlist = []
        for file in df['Wins']:
            winlist.append(file)

        losslist = []
        for name2 in df['Losses']:
            losslist.append(name2)

        winpercentage = []
        for name3 in df['Win Percentage']:
            winpercentage.append(name3)
        return winlist, losslist, winpercentage


    def teammt(self):
        for i in self.filelist:
            if str(i)==str(i):
                self.filelist.remove(str(i))

        for w in self.filelist:
            df2 = pd.read_csv(str(w), encoding='latin-1', names=['Player','Team', 'Touchdowns', 'Interceptions'])
            for playerval in df2['Player']:
                for teamval in df2['Team']:
                    self.playerlist = {playerval: teamval}
            break