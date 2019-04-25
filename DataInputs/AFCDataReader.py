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
for name in df8['Name']:
    teamrosterBufflaos.append(name)

positionsBufflaos = []
for pos8 in df8['Position']:
    positionsBufflaos.append(pos8)

teamValueBufflaos = "The Bufflaos"
teamvaluesAFC.append(teamValueBufflaos)

#########################################################
# Reading of data for the AFC North
########################################################


# Reading of Data for the Baltimore Ravens
df9 = pd.read_csv("Data/AFCDB/AFCNorth/TheBaltimoreRavens.csv", encoding="latin-1", names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterRavens = []
for name in df9['Name']:
    teamrosterRavens.append(name)

positionsRavens = []
for pos9 in df9['Position']:
    positionsRavens.append(pos9)

teamvalueRavens = "The Baltimore Ravens"
teamvaluesAFC.append(teamvalueRavens)

# Reading of Data for the Pittsburgh Steelers
df10 = pd.read_csv("Data/AFCDB/AFCNorth/ThePittsburghSteelers.csv", encoding="latin-1", names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterSteelers = []
for name in df10['Name']:
    teamrosterSteelers.append(name)

positionsSteelers = []
for pos9 in df10['Position']:
    positionsSteelers.append(pos9)

teamvalueSteelers = "The Pittsburgh Steelers"
teamvaluesAFC.append(teamvalueSteelers)


# Reading of Data for the Cleavland Browns
df11 = pd.read_csv("Data/AFCDB/AFCNorth/TheClevlandBrowns.csv", encoding="latin-1", names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterBrowns = []
for name in df11['Name']:
    teamrosterBrowns.append(name)

positionsBrowns = []
for pos11 in df11['Position']:
    positionsBrowns.append(pos11)

teamValueBrowns = "The Cleavland Browns"
teamvaluesAFC.append(teamValueBrowns)

# Reading of Data for the Cincinnati Bengals
df12 = pd.read_csv("Data/AFCDB/AFCNorth/TheCleavlandBrowns.csv", encoding="latin-1", names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterBengals = []
for name in df12['Name']:
    teamrosterBengals.append(name)

positionsBengals = []
for pos12 in df12['Position']:
    positionsBengals.append(pos12)

teamvalueBengals = "The Cincinnati Bengals"
teamvaluesAFC.append(teamvalueBengals)

##########################################################################################
# Reading of data for the AFC South
##########################################################################################

# Reading of Data for the Houston Texans
df13 = pd.read_csv("Data/AFCDB/AFCSouth/TheHoustonTexans.csv", encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterTexans = []
for name in df13['Name']:
    teamrosterTexans.append(name)

positionsTexans = []
for pos13 in df13['Position']:
    positionsTexans.append(pos13)

teamvalueTexans = "The Houston Texans"
teamvaluesAFC.append(teamvalueTexans)

# Reading of Data for the Tennessee titans
df14 = pd.read_csv("Data/AFCDB/AFCSouth/TheTennesseeTitans.csv", encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrostertitans = []
for name in df14['Name']:
    teamrostertitans.append(name)

positionsTitans = []
for pos14 in df['Position']:
    positionsTitans.append(pos14)


teamvalueTitans = "The Tennessee Titans"
teamvaluesAFC.append(teamvalueTitans)

# Reading of data for the Indianpolis colts

df15 = pd.read_csv("Data/AFCDB/AFCSouth/TheIndianpolisColts.csv", encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterColts = []
for name in df15['Name']:
    teamrosterColts.append(name)

positionsColts = []
for pos15 in df15['Position']:
    positionsColts.append(pos15)

teamvalueColts = "The Indianpolis colts"
teamvaluesAFC.append(teamvalueColts)

# Reading of data for Jacksonville Jaguars.

df16 = pd.read_csv("Data/AFCDB/AFCSouth/TheJacksonvilleJaguars.csv", encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterJaguars = []
for name in df16['Name']:
    teamrosterJaguars.append(name)

positionsJaguars = []
for pos16 in df16['Position']:
    positionsJaguars.append(pos16)

teamvalueJaguars = "The Jacksonville Jaguars"
teamvaluesAFC.append(teamvalueJaguars)

# End of reading of data for
# all AFC teams within the AFC Division.