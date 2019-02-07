import pandas as pd
from sklearn import *
import tensorflow as tf
import numpy as np


class DataLoop:
    def __init__(self):
        self.filelist = {}

    def fileloop(self, file):
        df = pd.read_csv(f"{file}", encoding="latin-1", names=['Wins', 'Losses', 'Win Percentage'])

        winlist = []
        for file in df['Wins']:
            winlist.append(file)

        losslist = []
        for name2 in df['Losses']:
            losslist.append(name2)

        winpercentage = []
        for name3 in df['Win Percentage']:
            winpercentage.append(name3)