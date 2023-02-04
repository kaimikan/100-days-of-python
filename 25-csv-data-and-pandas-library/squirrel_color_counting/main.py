import pandas

# diy solution - kind of all over the place but stackoverflow is all knowing
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_color_distribution = squirrel_data["Primary Fur Color"].value_counts().to_dict()
print(squirrel_color_distribution)
print(squirrel_color_distribution.keys())
print(squirrel_color_distribution.values())

color_data_frame = pandas.DataFrame(pandas.Series(squirrel_color_distribution))
color_data_frame = color_data_frame.reset_index()
color_data_frame.columns = ["Fur Color", "Count"]
# color_data_frame.rename(columns={list(color_data_frame)[0]: 'Fur Colors'}, inplace=True)
color_data_frame.to_csv("squirrel_colors.csv")
print(color_data_frame)

# course solution - not a fan
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
