import tensorflow as tf
import numpy as np
import pandas as pd

class PlayerWinClassifier:
    def __init__(self, team, player, draftyear, wlratioteam):
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
        self.wlratioteam = wlratioteam

    def pxwinloss(self):
        xw = 0
        xl = 0
        wlamount = []
        for playerrvar in self.wlratioteam:
            if playerrvar == 'win':
                wlamount.append('W')
                xw += 1
            elif playerrvar == 'loss':
                wlamount.append('L')
                xl += 1

        # Sum of the tgame, where t and subscript game
        # represents the amount of games played by the team.
        tgame = len(wlamount)

        # final calculation of the win/loss ratio for player node
        # of the neural network.
        pxformula = pow(2, xw - xl / tgame)
        return pxformula

    def deltapxwinloss(self):
        deltaxw = 0
        deltaxl = 0
        deltawlamount = []

        # finds the parameters of Deltaxl and Deltaxw, Deltaxl for losses for the team,
        # and appends those into deltawlamount, for finding Deltatgame
        for win in self.wlratioteam:
            if win == 'win':
                deltawlamount.append('DeltaW')
                deltaxw += 1
            elif win == 'loss':
                deltawlamount.append('DeltaL')
                deltaxl += 1

        # finding Deltatgame
        Deltatgame = len(deltawlamount)
        Deltapx = deltaxw - deltaxl / Deltatgame
        return Deltapx

    def classified(self):
        print(f"Player Name: {self.player}\nWin/Loss Ratio: {self.pxwinloss()}")
        print('--------------------------------------------------------------------')
        print(f"Player Name: {self.player}\nDelta Win/Loss Ratio: {self.deltapxwinloss()}")
