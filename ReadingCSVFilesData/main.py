# with open('weather-data.csv') as csvfile:
#     data = csvfile.readlines()
#     print(data)

# import csv
#
# with open('weather-data.csv') as csvfile:
#     data = csv.reader(csvfile)
#     next(data)
#     temperatures = []
#     for row in data:
#         print(row)
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
# data = pandas.read_csv("weather-data.csv")

# temp_list = data["temp"].tolist()
# print(temp_list)
# sum_of_temps = 0
# for temp in temp_list:
#     sum_of_temps += temp
#
# print(sum_of_temps)
# avg = sum_of_temps / len(temp_list)
# print(avg)

# avg = sum(temp_list) / len(temp_list)
# print(avg)

# print(f"Sum: {data['temp'].sum()}")
# print(f"Mean: {data['temp'].mean()}")
# print(f"Max: {data['temp'].max()}")

# Get data in row
# print(data[data.day == "Monday"])

# Get data row where the temperature is minimum
# print(data[data.temp == data.temp.min()])

# Get data row where the temperature is maximum
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# temp_in_c = monday.temp
# temp_in_f = (temp_in_c * 9 / 5) + 32
# print(temp_in_f)

squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Data.csv')

# primary_fur_color = squirrel_data['Primary Fur Color']
# data_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "count": primary_fur_color.value_counts().values
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("squirrel_count.csv")

grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count1.csv")
