import pandas as pd
import numpy as np
from sklearn import *
import tensorflow as tf


# Team Values AFC in this case.
teamvaluesAFC = []


# Reading of data for the AFC West.
####################################

# Reading of Data for the chiefs in this case.
df = pd.read_csv('Data/AFCDB/AFCWest/TheChiefsDB.csv', encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterChiefs = []
count = 0
teamrosterkeysChiefs = []
for name in df['Name']:
    teamrosterChiefs.append(name)
    count = count + 1
    teamrosterkeysChiefs.append(count)

positionsChiefs = []
for pos in df['Position']:
    positionsChiefs.append(pos)

teamvalueChiefs = "The Chiefs"
teamvaluesAFC.append(teamvalueChiefs)
teamdicChiefs = {}
for i in teamrosterkeysChiefs:
    teamdicChiefs = {teamrosterkeysChiefs[i - 1]: teamrosterChiefs[i - 1]}

# Reading of the data for the Broncos
df2 = pd.read_csv('Data/AFCDB/AFCWest/TheBroncosDB.csv', encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterBroncos = []
count2 = 0
teamrosterKeysBroncos = []
for name in df2['Name']:
    teamrosterBroncos.append(name)
    count2 = count2 + 1
    teamrosterKeysBroncos.append(count2)

positionsBroncos = []
for pos2 in df2['Position']:
    positionsBroncos.append(pos2)

teamvalueBroncos = "The Broncos"
teamvaluesAFC.append(teamvalueBroncos)
teamdicBroncos = {}
for i2 in teamrosterKeysBroncos:
    teamdicBroncos = {teamrosterKeysBroncos[i2 - 1]: teamrosterBroncos[i2 - 1]}


