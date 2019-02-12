import numpy
import sklearn
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
df5 = pd.read_csv("Data/NFCDB/NFCWestDB/LARamsDB.csv", encoding="latin-1", names=['Name', 'Position', 'Team', 'Position > 1'])
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

# Reading of data for the Seattle Seahawks
df6 = pd.read_csv("Data/NFCDB/NFCWestDB/SeattleSeahawksDB.csv", encoding="latin-1", names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterSeattleSeahawks = []
teamrosterkeysSeattleSeahawks = []
count6 = 0
for name in df6['Name']:
    teamrosterSeattleSeahawks.append(name)
    count6 = count6 + 1
    teamrosterkeysSeattleSeahawks.append(count6)

positionsSeattleSeahawks = []
for pos6 in df6['Position']:
    positionsSeattleSeahawks.append(pos6)

teamvalSeattleSeahawks = "Seattle Seahawks";
teamvalues.append(teamvalSeattleSeahawks)
teamdicSeattleSeahawks = {}
for i6 in teamrosterkeysSeattleSeahawks:
    teamdicSeattleSeahawks = {teamrosterkeysSeattleSeahawks[i6-1]: teamrosterSeattleSeahawks[i6 - 1]}

# Arizona Cardinals Data Reading
df7 = pd.read_csv("Data/NFCDB/NFCWestDB/AirzonaCardinalsDB.csv", encoding="latin-1", names=['Name','Position', 'Team', 'Position > 1'])
teamrosterAirzonaCardinals = []
teamrosterkeyValsAirzonaCardinals = []
count7 = 0
for name in df7['Name']:
    teamrosterAirzonaCardinals.append(name)
    count7 = count7 + 1
    teamrosterkeyValsAirzonaCardinals.append(count7)

positionsAirZonaCardinals = []
for pos7 in df7['Position']:
    positionsAirZonaCardinals.append(pos7)


teamvalAirzonaCardinals = "Airzona Cardinals"
teamvalues.append(teamvalAirzonaCardinals)
teamdicAirzonaCardinals = {}
for i7 in teamrosterkeyValsAirzonaCardinals:
    teamdicAirzonaCardinals = {teamrosterkeyValsAirzonaCardinals[i7 - 1]: teamrosterAirzonaCardinals[i7 - 1]}


# 49ers data reading for the team.
df8 = pd.read_csv("Data/NFCDB/NFCWestDB/49ersDB.csv", encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamroster49ers = []
count8 = 0
teamrosterkeys49ers = []
for name in df8['Name']:
    teamroster49ers.append(name)
    count8 = count8 + 1
    teamrosterkeys49ers.append(count8)

positions49ers = []
for pos8 in df8['Positions']:
    positions49ers.append(pos8)

teamval49ers = "The 49ers"
teamvalues.append(teamval49ers)
teamdic49ers = {}
for i8 in teamrosterkeys49ers:
    teamdic49ers = {teamrosterkeys49ers[i8 - 1]: teamrosterkeys49ers[i8 - 1]}

# NFC South Data reading
#########################################

# Saints data reading
df9 = pd.read_csv("Data/NFCDB/NFCSouthDB/SaintsDB.csv", encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrostersaints = []
count9 = 0
teamrosterkeyssaints = []
for name in df9['Name']:
    teamrostersaints.append(name)
    count9 = count9 + 1
    teamrosterkeyssaints.append(count9)

positionsSaints = []
for pos8 in df9['Position']:
    positionsSaints.append(pos8)

teamvaluesaints = "The Saints"
teamvalues.append(teamvaluesaints)
teamdicsaints = {}
for i9 in teamrosterkeyssaints:
    teamdicsaints = {teamrosterkeyssaints[i9 - 1]: teamrostersaints[i9 - 1]}

# Reading of data for Atlanta Falcons
df10 = pd.read_csv("Data/NFCDB/NFCSouthDB/AtlantaFalconsDB.csv", encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterAtlantaFalcons = []
teamrosterkeysAtlantaFalcons = []
count10 = 0
for name in df10['Name']:
    teamrosterAtlantaFalcons.append(name)
    count10 = count10 + 1
    teamrosterkeysAtlantaFalcons.append(count10)

positionsAtlantaFalcons = []
for pos10 in df10['Positions']:
    positionsAtlantaFalcons.append(pos10)

teamvalueFalcons = "Atlanta Falcons"
teamvalues.append(teamvalueFalcons)
teamdicFalcons = {}
for i10 in teamrosterkeysAtlantaFalcons:
    teamdicFalcons = {teamrosterkeysAtlantaFalcons[i10 - 1]: teamrosterAtlantaFalcons[i10 - 1]}

