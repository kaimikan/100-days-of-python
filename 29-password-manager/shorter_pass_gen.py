# just adding it for safekeeping
# this is fancier, but I decided to keep the longer one in the actual program
from random import randint, choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_letters = [letters[randint(0, randint(5, 10) - 1)] for i in range(0, randint(5, 10))]
password_symbols = [symbols[randint(0, randint(1, 5) - 1)] for i in range(0, randint(1, 5))]
password_numbers = [symbols[randint(0, randint(1, 5) - 1)] for i in range(0, randint(1, 5))]
password_list = password_letters + password_symbols + password_numbers
shuffle(password_list)

password = "".join(password_list)

print(password)
