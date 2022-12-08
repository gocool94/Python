import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


gray_squirrels = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels = len(data[data['Primary Fur Color'] == 'Black'])


data_dict = {
    "Fun color":["Grey","Cinnamon","Black"],
    "Count of values":[gray_squirrels,red_squirrels,black_squirrels]
}

print(data_dict)
final = pd.DataFrame(data_dict)
print(final)