import tensorflow as tf
import numpy as np
import pandas as pd


class PlayerWinClassifier:
    def __init__(self, team, player, draftyear):
        # for the classifacation of
        # the amount of time the player has
        # been on the team for.
        self.draftyear = draftyear
        self.team = team
        self.player = player

        # for the amount of time the team has
        # been around for.
        self.teamtime = []
        self.teamwinsloss = {}

    def pxwinloss(self):
        xw = 0
        xl = 0
        wlamount = []
        playervar = self.draftyear
        for playervar in self.teamwinsloss:
            for loss in playervar:
                if loss == 'win':
                    xw += 1
                    wlamount.append('W')
                elif loss == 'loss':
                    xl += 1
                    wlamount.append('L')

        # Sum of the tgame, where t and subscript game
        # represents the amount of games played by the team.
        tgame = np.sum(len(wlamount))

        # final calculation of the win/loss ratio for player node
        # of the neural network.
        pxformula = xw - xl / tgame
        return pxformula

    def deltapxwinloss(self):
        deltaxw = 0
        deltaxl = 0
        deltawlamount = []

        # finds the parameters of Deltaxl and Deltaxw, Deltaxl for losses for the team,
        # and appends those into deltawlamount, for finding Deltatgame
        for win in self.teamwinsloss:
            for loss in win:
                if loss == 'win':
                    deltawlamount.append('DeltaW')
                    deltaxw += 1
                elif loss == 'loss':
                    deltawlamount.append('DeltaL')
                    deltaxl += 1

        # finding Deltatgame
        Deltatgame = np.sum(len(deltawlamount))

        Deltapx = deltaxw - deltaxl / Deltatgame
        return Deltapx


    def playerSkillFunction(self):
        sx = 0
        xseason = 0
        nseason = len(self.teamwinsloss)
        xseasonprev = xseason - 1
        omegaplayertime = 0

    # function used for finding the omegaplayertime parameter.
    def omegaplayertime(self, pdraft, nseason):
        return nseason - pdraft





