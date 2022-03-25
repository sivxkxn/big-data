import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import matplotlib.pyplot as plt
brainFile = 'brainsize.txt' 
brainFrame = pd.read_csv(brainFile)
menDf = brainFrame[(brainFrame.Gender == 'Male')] 
# womenDf = brainFrame[(brainFrame.Gender == 'Female')]
mcorr = menDf.corr() 
sns.heatmap(mcorr)
plt.savefig('attribute_correlations2.png', tight_layout=True) 
# print(womenDf.corr(method='pearson'))
# menDf = brainFrame[(brainFrame.Gender == 'Male')] 
# womenDf = brainFrame[(brainFrame.Gender == 'Female')]
# womenMeanSmarts = womenDf[["PIQ", "FSIQ", "VIQ"]].mean(axis=1) 
# plt.scatter(womenMeanSmarts, womenDf["MRI_Count"]) 
# plt.show() 
# print(menDf)
# print(womenDf)