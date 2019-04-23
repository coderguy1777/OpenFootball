import pandas as pd
from NNFiles import PlayerClassifier

winli = ['win','loss', 'win','loss', 'loss','win', 'win','loss', 'loss','loss', 'loss','loss']

parser = PlayerClassifier.PlayerWinClassifier(wlratioteam=winli, draftyear="1988", team="Cowboys", player="Tom")
x = parser.deltapxwinloss()
print(x)
y = parser.pxwinloss()
print(y)