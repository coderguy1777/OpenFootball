import numpy
import pandas as pd

# Dallas Cowboys Dataset Roster
df = pd.read_csv('Data/NFCDB/NFCEastDB/DallasCowboysDB.csv', encoding="latin-1", names=['Name', 'Position', 'Team', 'Positions > 1'])
teamroster = []
teamrosterkeys = []
count = 0
for name in df['Name']:
    count = count + 1
    teamroster.append(name)
    teamrosterkeys.append(count)

positions = []
for pos in df['Position']:
    positions.append(pos)

teamvalcowboy = "Dallas Cowboys"
teamvalues = []
teamvalues.append(teamvalcowboy)
teamdiccowboys = {}

for i in teamrosterkeys:
    teamdiccowboys = {teamrosterkeys[i - 1]: teamroster[i - 1]}

# Philadelphia Eagles Dataset Roster
df2 = pd.read_csv('Data/NFCDB/NFCEastDB/PhildelphiaEaglesDB.csv', encoding="latin-1", names=['Name', 'Position', 'Team', 'Position > 1'])
teamrostereagles = []
teamrostereagleskeys = []
count2 = 0
for name in df2['Name']:
    teamrostereagles.append(name)
    count2 = count2 + 1
    teamrostereagleskeys.append(count2)

positionseagles = []
for pos2 in df2['Position']:
    positionseagles.append(pos2)

teamvaleagles = "Philadelphia Eagles"
teamvalues.append(teamvaleagles)
teamdiceagles = {}
for i2 in teamrostereagleskeys:
    teamdiceagles = {teamrostereagleskeys[i2 - 1]: teamrostereagles[i2 - 1]}

# New York Giants Dataset Roster
df3 = pd.read_csv('Data/NFCDB/NFCEastDB/NewYorkGiantsDB.csv', encoding="latin-1", names=['Name', 'Position', 'Team', 'Position > 1'])
teamrostergiants = []
teamrostergiantskeys = []
count3 = 0
for name in df3['Name']:
    teamrostergiants.append(name)
    count3 = count3 + 1
    teamrostergiantskeys.append(count3)

positiongiants = []
for pos3 in df3['Position']:
    positiongiants.append(pos3)

teamvalgiants = "The New York Giants"
teamvalues.append(teamvalgiants)
teamdicgiants = {}
for i3 in teamrostergiantskeys:
    teamdicgiants = {teamrostergiantskeys[i3 - 1]: teamrostergiants[i3 - 1]}

# Washington Redskins Dataset Roster
df4 = pd.read_csv('Data/NFCDB/NFCEastDB/RedskinsDB.csv', encoding="latin-1", names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterRedskins = []
teamrosterkeysRedskins = []
count4 = 0
for name in df4['Name']:
    teamrosterRedskins.append(name)
    count4 = count4 + 1
    teamrosterkeysRedskins.append(count4)

positionsredskins = []
for pos4 in df4['Position']:
        positionsredskins.append(pos4)

teamvalredskins = "Washington Redskins"
teamvalues.append(teamvalredskins)
teamdicredskins = {}
for i4 in teamrosterkeysRedskins:
    teamdicredskins = {teamrosterkeysRedskins[i4 - 1]: teamrosterRedskins[i4 - 1]}

# NFC West data reading.
######################################
# Reading of data for the Los Angeles Rams Roster
df5 = pd.read_csv("Data/NFCDB/NFCWestDB/LARamsDB.csv", encoding="latin-1", name=['Name', 'Position', 'Team', 'Position > 1'])

teamrosterLARams = []
teamrosterkeysLARams = []
count5 = 0
for name in df5['Name']:
    teamrosterLARams.append(name)
    count5 = count5 + 1
    teamrosterkeysLARams.append(count5)

positionsLARams = []
for pos5 in df5['Position']:
    positionsLARams.append(pos5)

teamvallarams = "Los Angeles Rams"
teamvalues.append(teamvallarams)
teamdiclarams = {}
for i5 in teamrosterkeysLARams:
    teamdiclarams = {teamrosterkeysLARams[i5 - 1]: teamrosterLARams[i5 - 1]}

teamvallarams = "Los Angeles Rams"
teamvalues.append(teamvallarams)
