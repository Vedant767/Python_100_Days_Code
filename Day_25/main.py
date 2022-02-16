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

data = pandas.read_csv('weather_data.csv')
temp_data = data["temp"].to_list()
print(mean(temp_data))