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

# Reading of data for the Panthers
df11 = pd.read_csv("Data/NFCDB/NFCSouthDB/PanthersDB.csv", encoding='latin-1', names=['Name', 'Positions', 'Team', 'Positions > 1'])
teamrosterPanthers = []
count11 = 0
teamrosterkeysPanthers = []
for name in df11['Name']:
    teamrosterPanthers.append(name)
    count11 = count11 + 1
    teamrosterkeysPanthers.append(count11)

positionsPanthers = []
for pos11 in df11['Position']:
    positionsPanthers.append(pos11)

teamvaluePanthers = "The Panthers"
teamvalues.append(teamvaluePanthers)
teamdicPanthers = {}
for i11 in teamrosterkeysPanthers:
    teamdicPanthers = {teamrosterkeysPanthers[i11 - 1]: teamrosterPanthers[i11 - 1]}

# Reading of data for the Buccaneers in this case
df12 = pd.read_csv('Data/NFCDB/NFCSouthDB/BuccaneersDB.csv', encoding='latin-1', names=['Name', 'Position', 'Team', 'Positions > 1'])
teamrosterBuccaneers = []
count12 = 0
teamrosterkeysBuccaneers = []
for name in df12['Name']:
    teamrosterBuccaneers.append(name)
    count12 = count12 + 1
    teamrosterkeysBuccaneers.append(count12)

positionsBuccaneers = []
for pos12 in df12['Positions']:
    positionsBuccaneers.append(pos12)

teamvalueBuccaneers = "The Buccaneers"
teamvalues.append(teamvalueBuccaneers)
teamdicBuccaneers = {}
for i12 in teamrosterkeysBuccaneers:
    teamdicBuccaneers = {teamrosterkeysBuccaneers[i12 - 1]: teamrosterBuccaneers[i12 - 1]}

# Reading of Data for the NFC North Teams and there respective divisions.
##################################################

# Reading of data for the Green Bay Packers
df13 = pd.read_csv('Data/NFCDB/NFCNorth/GreenbayPackersDB.csv', encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterGreenBayPackers = []
count13 = 0
teamrosterKeysGreenBayPackers = []
for name in df13['Name']:
    teamrosterGreenBayPackers.append(name)
    count13 = count13 + 1
    teamrosterKeysGreenBayPackers.append(count13)

positionsGreenBayPackers = []
for pos13 in df13['Position']:
    positionsGreenBayPackers.append(pos13)

teamvalueGreenBayPackers = "The Green Bay Packers"
teamvalues.append(teamvalueGreenBayPackers)
teamdicGreenBayPackers = {}

for i13 in teamrosterKeysGreenBayPackers:
    teamdicGreenBayPackers = {teamrosterKeysGreenBayPackers[i13 - 1]: teamrosterGreenBayPackers[i13 - 1]}

# Reading of data for the Vikings in this case
df14 = pd.read_csv('Data/NFCDB/NFCNorth/TheVikingsDB.csv', encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterVikings = []
count14 = 0
teamrosterKeysVikings = []
for name in df14['Name']:
    teamrosterVikings.append(name)
    count14 = count14 + 1
    teamrosterKeysVikings.append(count14)

positionsVikings = []
for pos14 in df14['Position']:
    positionsVikings.append(pos14)

teamvalueVikings = "The Vikings"
teamvalues.append(teamvalueVikings)
teamdicVikings = {}
for i14 in teamrosterKeysVikings:
    teamdicVikings = {teamrosterKeysVikings[i14 - 1]: teamrosterVikings[i14 - 1]}

# Reading of data for the Bears
df15 = pd.read_csv('Data/NFCDB/NFCNorth/TheBearsDB.csv', encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterBears = []
count15 = 0
teamrosterkeysBears = []
for name in df15['Name']:
    teamrosterBears.append(name)
    count15 = count15 + 1
    teamrosterkeysBears.append(count15)

positionsBears = []
for pos15 in df15['Position']:
    positionsBears.append(pos15)


teamvalueBears = "The Bears"
teamvalues.append(teamvalueBears)
teamdicBears = {}
for i15 in teamrosterkeysBears:
    teamdicBears = {teamrosterkeysBears[i15 - 1]: teamrosterBears[i15 - 1]}

# Reading of data for the Lions in this case
df16 = pd.read_csv('Data/NFCDB/NFCNorth/TheLionsDB.csv', encoding='latin-1', names=['Name', 'Position', 'Team', 'Position > 1'])
teamrosterLions = []
count16 = 0
teamrosterKeysLions = []
for name in df16['Name']:
    teamrosterLions.append(name)
    count16 = count16 + 1
    teamrosterKeysLions.append(count16)

positionsLions = []
for pos16 in df16['Position']:
    positionsLions.append(pos16)

teamvalueLions = "The Lions"
teamvalues.append(teamvalueLions)
teamdicLions = {}
for i16 in teamrosterKeysLions:
    teamdicLions = {teamrosterKeysLions[i16 - 1]: teamrosterLions[i16 - 1]}

# End of NFC Data Reading for all the NFC Teams.