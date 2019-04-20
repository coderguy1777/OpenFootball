import numpy as np
import tensorflow as tf
from NNFiles import PlayerClassifier
import pandas as pd

class PlayerRanks:
    def __init__(self, teamsize, team, playerNode, playerName, draftVar):
        self.teamsize = teamsize
        self.playerName = playerName
        self.playerNode = playerNode
        self.team = team
        self.draftVar = draftVar
        self.player = PlayerClassifier.PlayerWinClassifier(team=self.team, player=playerName, draftyear=self.draftVar)
        self.playerNode = playerNode
        self.playerStats = []

    def playerSkill(self):
        # for the ranking of players on the team
        # that they are on
        ranksum = []

        # Classifing variable
        playerclassfied = 0

        loopvar = 0
        while loopvar + 1 <= self.teamsize:
            playerclassfied = self.player.pxwinloss()
            ranksum.append(playerclassfied)

        tempvar = 0
        for i in ranksum:
            tempvar = i
            if i < i + 1:
                tempvar = i + 1
                ranksum.append(i)
                ranksum.pop(tempvar)
            elif i > i + 1:
                tempvar = i
                ranksum.append(i + 1)
                ranksum.pop(tempvar)
            ranksum.append(tempvar)

        return ranksum

    def playerGameStats(self):
        pass

