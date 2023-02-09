# FileNotFound
# with open("this_file_doesnt_exist.txt") as file:
#     file.read()
try:
    file = open("this_file_doesnt_exist.txt")
    a_dict = {"key": "value"}
    # value = a_dict["non_existent_key"]
except FileNotFoundError:
    # we create the file
    file = open("this_file_doesnt_exist.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    # raise TypeError("I made this error with the purpose of trolling. We do a little trolling")
    file.close()
    print("file was closed.")

# # KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        post['Likes']
    except KeyError:
        post['Likes'] = 0
    else:
        total_likes = total_likes + post['Likes']

print(total_likes)

# # IndexError
# fruits = ["apple", "banana", "pear"]
# fruit = fruits[4]

# # TypeError
# text = "abc"
# print(text + 5)

# # Index Error
fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    index
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)

# # ValueError
height = float(input("Height (meters): "))
weight = float(input("Weight (kilograms): "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

# height ** 2 = height * height
bmi = weight / height ** 2
print(bmi)
