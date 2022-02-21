from audioop import avg
import csv
import pandas
from statistics import mean
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv('weather_data.csv')
# temp_data = data["temp"].to_list()
# print(mean(temp_data))

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur1 = len(data[data['Primary Fur Color'] == 'Black'])
fur2 = len(data[data['Primary Fur Color'] == 'Gray'])
fur3 = len(data[data['Primary Fur Color'] == 'Cinnamon'])
print(fur2)
print(fur3)
print(fur1)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [fur2, fur3, fur1]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")