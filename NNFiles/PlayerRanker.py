import numpy as np
import tensorflow as tf
import pandas as pd
from NNFiles import BasePlayerSkills as bps

class PlayerSkill:
    def __init__(self, playername, downs, cintercepts, incintercepts, cpasses, incpasses, tpasses, tintercepts, cwk, cwl, TDc, TDinc, NTD):
        self.playername = playername
        self.downs = downs
        self.cintercepts = cintercepts
        self.incintercepts = incintercepts
        self.cpasses = cpasses
        self.incpasses = incpasses
        self.tpasses = tpasses
        self.tintercepts = tintercepts
        self.cwk = cwk
        self.cwl = cwl
        self.TDc = TDc
        self.TDinc = TDinc
        self.NTD = NTD
        self.playerskillval = 0

    def pskill(self):
        interceptpc = bps.intrcptps(self.cintercepts, self.incintercepts, self.tintercepts)
        passpc = bps.passpercent(self.cpasses, self.incpasses, self.tpasses)
        downs = self.downs / self.cwl
        tdpct = bps.tdpct(self.TDc, self.TDinc, self.NTD)
        self.playerskillval = np.exp(self.cwl, (np.sqrt(interceptpc + passpc + tdpct))) / downs

    def findtdpct(self):
        return bps.tdpct(self.TDc, self.TDinc, self.NTD)

    def findintcpct(self):
        return bps.intrcptps(self.cintercepts, self.incintercepts, self.tintercepts)