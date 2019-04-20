import tensorflow as tf
import numpy as np
from NNFiles import PlayerClassifier
import pandas as pd

class TeamDivRanker:
    def __init__(self, teamObj):
        self.teamObj = teamObj
        self.divisionDic = {}
        self.teamSkill = 0

    def divRanker(self):
        pass
