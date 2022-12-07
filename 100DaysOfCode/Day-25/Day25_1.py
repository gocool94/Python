"""
with open('weather_data.csv') as data_file:
    data = data_file.readlines()
    print(data)

"""

import pandas as pd
import csv
"""
with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temparatures = []
    for row in data:
        if(row[1]!='temp'):
            temparatures.append(int(row[1]))
    print(temparatures)
    
"""

data = pd.read_csv('weather_data.csv')


data_dict = data.to_dict()
data_list = data["temp"].to_list()
print(data_dict)
print(data_list)


print(data["temp"].mean())
print(data["temp"].max())
sum = 0
for i in data_list:
    sum+=i

average = sum/len(data_list)
print(average)

print(data.temp)

#get the row

#print(data[data.temp==data["temp"].max()]) # getting the maximum temperature

monday = data[data.day=='Monday']
mondays_temp = int(monday.temp)
print(mondays_temp)

monday_temp_F = mondays_temp * 9/5 +32
print(monday_temp_F)