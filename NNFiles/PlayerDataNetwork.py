import numpy as np
from sklearn import *
import tensorboard as tb
import tensorflow as tf

class PlayerNetwork:
    def __init__(self, inputs, positions, teamname):
        self.dic = {}
        self.inputs = inputs
        self.positions = positions
        self.teamname = teamname
        self.teamdb = {}

    def mainnet(self):
        playerteammap = []
        dic2 =  {}
        print(str(self.teamname))
        for (i, x) in enumerate(self.inputs):
            self.dic = {x: self.positions[i]}
            dic2 = {self.teamname: self.dic}
            playerteammap.append(dic2)

        if self.teamname == 'Washington Redskins' or self.teamname == 'Dallas Cowboys' or self.teamname == 'Philadelphia Eagles' or self.teamname == 'The New York Giants':
            divname = 'NFC East'
            self.teamdb = {divname: list(playerteammap)}
            print(f"{self.teamdb}")
        if self.teamname == 'Seattle Seahawks' or self.teamname == 'Los Angeles Rams' or self.teamname == 'The 49ers' or self.teamname == 'The Arizona Cardinals':
            divnamewest = 'NFC West'
            self.teamdb = {divnamewest: list(playerteammap)}
            print(self.teamdb)
        return self.teamdb, self.dic, dic2


    def indivdiualplayerstatsnetwork(self):
        i = 0
