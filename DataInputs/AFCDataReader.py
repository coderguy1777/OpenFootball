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
positionsChiefs.pop(0)
teamrosterChiefs.pop(0)

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
positionsBroncos.pop(0)
teamrosterBroncos.pop(0)

# Reading of data for The Raiders in this case.
df3 = pd.read_csv('Data/AFCDB/AFCWest/TheRaidersDB.csv', encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterRaiders = []

for name in df3['Name']:
    teamrosterRaiders.append(name)
teamrosterRaiders.pop(0)

positionsRaiders = []
for pos3 in df3['Position']:
    positionsRaiders.append(pos3)
positionsRaiders.pop(0)

teamvalueRaiders = "The Raiders"
teamvaluesAFC.append(teamvalueRaiders)

# Reading of Data for The Chargers in this case.
df4 = pd.read_csv('Data/AFCDB/AFCWest/TheChargersDB.csv', encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterChargers = []

for name in df4['Name']:
    teamrosterChargers.append(name)
teamrosterChargers.pop(0)

positionsChargers = []
for pos4 in df4['Position']:
    positionsChargers.append(pos4)
positionsRaiders.pop(0)

teamvalueChargers = "The Chargers"
teamvaluesAFC.append(teamvalueChargers)

# Reading of data for teams within AFC East in this case.
#############################################################

# Reading of data for the New England Patriots in this case.
df5 = pd.read_csv("Data/AFCDB/AFCEast/TheNewEnglandPatriotsDB.csv", encoding='latin-1', names=['Name', 'Position', 'Team' , 'Position > 1'])
teamrosterNewEnglandPatriots = []
for name in df5['Name']:
    teamrosterNewEnglandPatriots.append(name)
teamrosterNewEnglandPatriots.pop(0)

positionsPatriots = []
for pos5 in df5['Position']:
    positionsPatriots.append(pos5)
positionsPatriots.pop(0)

teamvaluePatriots = "The New England Patriots"
teamvaluesAFC.append(teamvaluePatriots)

# Reading of data for the New York Jets in this case.
df6 = pd.read_csv('Data/AFCDB/AFCEast/TheNewYorkJetsDB.csv', encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrostertheJets = []
for name in df6['Name']:
    teamrostertheJets.append(name)
teamrostertheJets.pop(0)

positionstheJets = []
for pos6 in df6['Position']:
    positionstheJets.append(pos6)
positionstheJets.pop(0)

teamvalueJets = "The New York Jets"
teamvaluesAFC.append(teamvalueJets)

# Reading of data for the Miami Dolphins
df7 = pd.read_csv("Data/AFCDB/AFCEast/TheMiamiDolphinsDB.csv", encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterDolphins = []

for name in df7['Name']:
    teamrosterDolphins.append(name)
teamrosterDolphins.pop(0)

positionsDolphins = []
for pos7 in df7['Position']:
    positionsDolphins.append(pos7)
positionsDolphins.pop(0)

teamValueDolphins = "The Miami Dolphins"
teamvaluesAFC.append(teamValueDolphins)

# Reading of data for the Buffalos in this case
df8 = pd.read_csv("Data/AFCDB/AFCEast/TheBufflaos.csv", encoding="latin-1", names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterBufflaos = []