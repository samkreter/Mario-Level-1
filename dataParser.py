import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


main = pd.read_csv("timings/m1.csv",header=None)
death = pd.read_csv("timings/d1.csv",header=None)
conf = pd.read_csv("timings/tconf.csv",header=None)




#Death Stats
print("Average time to solution: ",death[0].mean() / 60, " mins")
print("Average number of attemps: ",death[1].mean(), " attemps")


for index in m[m[0] == 0].index.tolist():
    max_scores = m

