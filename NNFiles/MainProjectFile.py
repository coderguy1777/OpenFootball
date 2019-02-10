import matplotlib.pyplot as plt
import pandas as pd
from sklearn import *
import tensorflow as tf
from DataInputs import DataFileLoop

filenamelist = []
filenamelist.append('NetworkData/output-onlinerandomtools.csv')
filenamelist.append('NetworkData/testfile.csv')

for fileval in filenamelist:
    filelooper.fileloop(fileval)
    filelooper.teammt()
