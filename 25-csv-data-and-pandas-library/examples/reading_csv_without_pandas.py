import csv
# CSV - comma separated values
import re

# regex - to check if row string for temperature contains actual letters


# with open("weather_data.csv") as data_file:
#     contents = data_file.read().splitlines()
#     data = contents
# print(data)

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if not re.search('[a-zA-Z]', row[1]):
            # the above re.search looks for any letters in the string
            # (we want to only add the temperature numbers, not the temp heading text)
            temperatures.append(int(row[1]))
        # print(row)
    print(temperatures)
