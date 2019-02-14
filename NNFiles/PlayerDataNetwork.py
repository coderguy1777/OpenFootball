import numpy as np
from sklearn import *
import tensorboard as tb
import tensorflow as tf

class PlayerNetwork:
    def __init__(self, inputs, teamname):
        self.dic = {}
        self.inputs = inputs
        self.teamname = teamname
        self.teamdb = {}
        self.nfcdb = {}
        self.nfcwestdb = {}
        self.afcdb = []

    def datasort(self):
        testin = []
        playerteammap = []
        dic2 = {}
        for (i, x) in enumerate(self.inputs):
            self.dic[x] = self.inputs[x]
            dic2 = {self.teamname: self.dic}
            playerteammap.append(dic2)
            testin.append(dic2)

        if self.teamname == 'Washington Redskins' or self.teamname == 'Dallas Cowboys' or self.teamname == 'Philadelphia Eagles' or self.teamname == 'The New York Giants':
            divname = 'NFC East'
            self.nfcdb = {self.teamname: list(playerteammap)}

        if self.teamname == 'Seattle Seahawks' or self.teamname == 'Los Angeles Rams' or self.teamname == 'The 49ers' or self.teamname == 'The Arizona Cardinals':
            divnamewest = 'NFC West'
            self.teamdb = {divnamewest: list(playerteammap)}
            self.nfcwestdb = [(self.teamname, self.teamdb)]

        if self.teamname == 'The Saints' or self.teamname == 'Atlanta Falcons' or self.teamname == 'The Panthers' or self.teamname == 'The Buccaneers':
            divnamesouth = 'NFC South'
            self.teamdb = {divnamesouth: list(playerteammap)}
            print(self.teamdb)

        if self.teamname == 'The Green Bay Packers' or self.teamname == 'The Vikings' or self.teamname == 'The Bears' or self.teamname == 'The Lions':
            divnamenorth = 'NFC North'
            self.teamdb = {divnamenorth: list(playerteammap)}
            print(self.teamdb)
        return dic2
