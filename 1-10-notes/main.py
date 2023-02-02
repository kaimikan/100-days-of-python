# PRINTS & INPUTS
# name = input("What's your name? ")
# you can also do stuff like this
# print("Hello, " + input("What's your name? ") + "!")
# /n is new line
print("tes\ning")
print('''
multi-block
string
''')
# print(len(input("Type something ")))

# Data Types

# Strings
print("Hello"[4])
print("123" + "456")

# Integer
print(123 + 456)

# _ in integers is just for us to visualize better
print(123_456_789)

# Float
print(3.14159)

# Boolean
print(True + False)  # 0 + 1

# Type Check
print(type(123))

# Type Conversion/Casting
new_int = 123
# this gives an error print(new_int + " test")
new_string = str(new_int)
print(new_string + " test")

print(float(new_int))
print(70 + float("100.5"))
print(str(70) + str(100))
# rounding numbers
print(round(8 / 3))
print(round(8 / 3, 2))
print(8 // 3)
print(type(8 // 3))
result = 4 / 2
result /= 2
print(result)

# f-Strings (notice the automatic casting of int to string)
print(f"the result is {result}")
print("{:.2f}".format(2.4))

# conditions if elif else
if 5 > 4 and 2 < 3:
    print("yo")
if 5 > 4 or 5 == 9999:
    print("ye")
if not 5 == 9999:
    print("ya")

# randomness
import random

random_integer = random.randint(1, 10)
print(random_integer)

# between 0.00000... and 0.99999...
random_float = random.random()
print(random_float)

# lists
letters = ["a", "b", "c", "d", "e"]
numbers = [1, 2, 3, 4, 5]
letters[0] = "Aa"
print(letters[0])
print(letters[-1])
letters.append("Ff")
print(letters[-1])
letters.extend(["Gg", "Hh", "Ii"])
print(len(letters))
letters_numbers_list = [letters, numbers]
print(letters_numbers_list)
print(letters_numbers_list[0][1])

print("Random choice " + random.choice(letters))
random.shuffle(letters)
print(letters)
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# LOOPS

letters = ["a", "b", "c"]
for letter in letters:
    print(letter)

for number in range(1, 11):
    print(number)

for number in range(3):
    print("yo")

for number in range(1, 11, 3):
    print(number)


# Functions
def my_function():
    print("Hello")
    print("Bye")


my_function()


def greeting(name, weather):
    print(f"yo, {name}!")
    print(f"the temperature outside is {weather}")


greeting(
    "name",
    "3 Celsius")

greeting(weather="50 Fahrenheit", name="bob")


def calculate_sum(a, b):
    """Calculate the sum of 2 numbers."""
    # docstring
    return a + b


print(calculate_sum(5, 3))

# tabs vs spaces identation
# spaces are preferred, most compilers offer to convert a tab to 4 spaces automatically

# Loop
water_level = 50
while water_level > 0:
    water_level -= 10
print(water_level)

# DICTIONARIES
definitions = {
    "bug": "an error in a program",
    "function": "an easily reusable piece of code",
    "loop": "the action of doing something over and over again",
    123: 456,
}

# retrieving items
print(definitions["bug"])
print(definitions[123])

# adding items
definitions["test"] = "this is a test add"

# create an empty dictionary
empty_dic = {}

# wipe and existing dictionary
# definitions = {}

# editing items
definitions[123] = 789

# loop through a dictionary
print("PRINT ALL")
for key in definitions:
    print(key)
    print(definitions[key])

# NESTING DICTIONARIES
nesting_example = {
    "english_alphabet": ["a", "b", ["C", "c"]],
    "europe": {
        "Bulgaria": "Sofia",
        "France": "Paris"
    }
}

travel_log_v1 = {
    "france": {
        "cities_visited": ["paris", "lille", "dijon"],
        "total_visits": 3
    },
}

travel_log_v2 = [{
    "country": "france",
    "cities_visited": ["paris", "lille", "dijon"],
    "total_visits": 3,
}]

# SCOPE
enemies = 3


def increase_enemy_amount():
    # global enemies
    # ^ not recommended to modify inside function
    # enemies += 1
    return enemies + 1


enemies = increase_enemy_amount()
print(enemies)

# constants - uppercase for easier readability
PI = 3.14159
