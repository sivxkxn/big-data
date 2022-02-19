# Code cell 1
# %matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium 
from matplotlib import colors
dataset_path = './crime.csv'
SF = pd.read_csv(dataset_path)
districts = np.unique(SF['PdDistrict'])
# print(list(colors.cnames.values())[0:len(districts)])
color_dict = dict(zip(districts, list(colors.cnames.values())[0:-1:len(districts)]))
# color_dict
map_osm = folium.Map(location=[SF['Y'].mean(), SF['X'].mean()], zoom_start = 12)
plotEvery = 50
obs = list(zip( SF['Y'], SF['X'], SF['PdDistrict']))
for el in obs[0:-1:plotEvery]:
    folium.CircleMarker(el[0:2], color=color_dict[el[2]], fill_color=el[2],radius=10).add_to(map_osm)
map_osm.save('m.html')
# print(map_osm)

# pd.set_option('display.max_rows', 20) #Visualize 10 rows
# SF['Month'] = SF['Date'].apply(lambda row: int(row[0:2]))
# SF['Day'] = SF['Date'].apply(lambda row: int(row[3:5]))
# del SF['IncidntNum']
# SF.drop('Location', axis=1, inplace=True)

# pd_districts = np.unique(SF['PdDistrict'])
# pd_districts_levels = dict(zip(pd_districts, range(len(pd_districts))))
# # print(pd_districts_levels)
# SF['PdDistrictCode'] = SF['PdDistrict'].apply(lambda row: pd_districts_levels[row])
# plt.scatter(SF['X'], SF['Y'], c=SF['PdDistrictCode'])
# plt.show()
# Crime0704 = SF.query('Month == 7 and Day == 4')
# print(Crime0704)
# Code cell 20
# print(SF.columns)

# AugustCrimes = SF[SF['Month'] == 8]
# AugustCrimes
# AugustCrimes = SF[SF['Month'] == 8]
# AugustCrimesB = SF[SF['Category'] == 'BURGLARY']
# len(AugustCrimesB)
# print(len(AugustCrimes))
# print(len(AugustCrimesB))
# print(SF['PdDistrict'].value_counts(ascending=True))
# print(SF['Month'][0:2])
# print(type(SF['Month'][0]))
# print(SF)
# print(SF)