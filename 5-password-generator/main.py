# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for letter in range(0, nr_letters):
    password += letters[random.randint(0, len(letters) - 1)]

for symbol in range(0, nr_symbols):
    password += symbols[random.randint(0, len(symbols) - 1)]

for number in range(0, nr_numbers):
    password += numbers[random.randint(0, len(numbers) - 1)]

print(password)

password = ""

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

all_characters = [letters, symbols, numbers]
total_characters = nr_letters + nr_symbols + nr_numbers

for character in range(0, total_characters):
    character_pool = random.randint(0, 2)
    pool_size = len(all_characters[character_pool])
    random_pool_character = random.randint(0, pool_size - 1)
    random_character = all_characters[character_pool][random_pool_character]
    password += random_character

print(password)

# you can also use random.choice(list)
print(random.choice(letters))
# you can also use random.shuffle(list)
random.shuffle(letters)
print(letters)
