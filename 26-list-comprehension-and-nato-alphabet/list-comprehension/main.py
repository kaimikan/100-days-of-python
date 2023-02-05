# WITHOUT list comprehension
numbers = [1, 2, 3]
new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# WITH list comprehension
# visualization: newer_list = [new_item for item in list]
newer_list = [n + 1 for n in numbers]
print(newer_list)
# yo, python very legit
name = "Imeme"
name_letters = [letter for letter in name]
print(name_letters)

double_numbers = [number * 2 for number in range(0, 5)]
print(double_numbers)

# conditional list comprehension
names = ["Bob", "Steve", "Phil", "Bill", "Joe"]
# visualization: short_names = [new_item for item in list if test]
short_names = [name for name in names if len(name) <= 3]
print(short_names)
capitalized_long_names = [name.upper() for name in names if len(name) > 3]
print(capitalized_long_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number * number for number in numbers]
# or
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# overlapping numbers
with open('file2.txt') as file:
    file_1_numbers = file.read().splitlines()

with open('file2.txt') as file:
    file_2_numbers = file.read().splitlines()

print(file_1_numbers)
print(file_2_numbers)

overlapping_numbers = [number for number in file_1_numbers if number in file_2_numbers]
print(overlapping_numbers)
