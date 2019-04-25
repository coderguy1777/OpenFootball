import pandas as pd
import math
from NNFiles import PlayerClassifier
import time

start = time.time()
df = pd.read_csv("WLRatio.csv", encoding='latin-1', names=['Wins', 'Losses'])

# seperation of the data into seperate columns from the csv file
# -----------------------------------------------------------------

# wins column
winsls = []
for win in df['Wins']:
    winsls.append(win)
winsls.pop(0)

# losses column
lossesls = []
for loss in df['Losses']:
    lossesls.append(loss)
lossesls.pop(0)

# sorting into the final list
finalls = []

# wins list
for i in winsls:
    finalls.append(i)

# losses list
for x in lossesls:
    finalls.append(x)

# sets up the parser
parser = PlayerClassifier.PlayerWinClassifier(wlratioteam=finalls, draftyear="1988", team="Cowboys", player="Tom")
print(parser.classified())