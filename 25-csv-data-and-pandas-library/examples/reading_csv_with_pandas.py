import pandas

# https://pandas.pydata.org/docs/reference/index.html
# https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

data = pandas.read_csv("weather_data.csv")
# DataFrame represents the entire table
print(type(data))
print(data["temp"])
# Series represents an entire column
print(type(data["temp"]))

# Data Conversion and manipulation
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
# average_temp = sum(temp_list) / len(temp_list)
average_temp = data["temp"].mean()
max_temp = data["temp"].max()
print(max_temp)

# Get Data in Columns
print(data["condition"])
# pandas automatically converts them to attributes
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp_fahrenheit = int(data[data.day == "Monday"].temp) * 9 / 5 + 32
print(monday_temp_fahrenheit)
# you can also convert the entire column to Fahrenheit
temps_F = data.temp * 9 / 5 + 32
# print(temps_F)

# Create a DataFrame from scratch
data_dict = {
    "students": ["Bob", "Job", "Knob"],
    "scores": [7, 2, 7]
}
student_data = pandas.DataFrame(data_dict)
print(student_data)
student_data.to_csv("student_data.csv")
