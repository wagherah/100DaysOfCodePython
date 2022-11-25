import pandas

# How to read data form csv file
# with open('weather_data.csv', 'r') as data_file:
#     data = csv.reader(data_file)
#     for obj in data:
#         print(obj)

# temperatures = []
# with open('weather_data.csv', 'r') as data_file:
#     data = csv.reader(data_file)

#     for obj in data:
#         if obj[1] == 'temp':
#             continue
#         temperatures.append(int(obj[1]))

# print(temperatures)

# instead of doing this tidious work for each column, we use pandas, which provides ease in dealing such conditions

# whole table is DataFrame in pandas
# each column is Series

data = pandas.read_csv('weather_data.csv')
temperatures_list = data['temp']
average = temperatures_list.mean()
# print(average)
# get data in  a column:
# data['temp']  or data.temp

# get data in a row:
# data[data.day=='Monday']

# creating a data_frame from scratch:
data_dict = {
    'students': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    'scores': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}
data = pandas.DataFrame(data_dict)
# saving the data frame in csv file
data.to_csv('students_data.csv')
