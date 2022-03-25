import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
brainFile = 'brainsize.txt' 
brainFrame = pd.read_csv(brainFile)
brainFrame.corr(method='pearson')
# menDf = brainFrame[(brainFrame.Gender == 'Male')] 
# womenDf = brainFrame[(brainFrame.Gender == 'Female')]
# womenMeanSmarts = womenDf[["PIQ", "FSIQ", "VIQ"]].mean(axis=1) 
# plt.scatter(womenMeanSmarts, womenDf["MRI_Count"]) 
# plt.show() 
# print(menDf)
# print(womenDf)