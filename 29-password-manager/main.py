from tkinter import *
from tkinter import messagebox
# we import messagebox even despite * since its a separate file
import random
import pyperclip

RED = "#d4483b"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# using code from day 5 (pretty epic)
# check shorter_pass_gen.py for another, shorter way to generate
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(5, 10)
    nr_symbols = random.randint(1, 5)
    nr_numbers = random.randint(1, 5)

    password = ""
    # Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    all_characters = [letters, symbols, numbers]
    total_characters = nr_letters + nr_symbols + nr_numbers

    for character in range(0, total_characters):
        character_pool = random.randint(0, 2)
        pool_size = len(all_characters[character_pool])
        random_pool_character = random.randint(0, pool_size - 1)
        random_character = all_characters[character_pool][random_pool_character]
        password += random_character

    # print(password)
    password_entry.delete(0, END)
    password_entry.insert(index=0, string=password)
    # copy password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(password) == 0 or len(website) == 0 or len(email) == 0:
        messagebox.showerror(title="Invalid Data", message="Some of the fields are missing")
    else:
        is_data_ok = messagebox.askokcancel(title=website, message=f"Details entered: "
                                                                   f"\nEmail: {email}"
                                                                   f""f"\nPassword: {password}\n")

        if is_data_ok:
            with open("website_accounts.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                email_entry.insert(index=0, string="example@gmail.com")
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

image_width = 200
image_height = 200
canvas = Canvas(width=image_width, height=image_height, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(image_width / 2, image_height / 2, image=lock_image)
canvas.grid(column=1, row=0)

# sticky="E"ast - sticks to right side of area
# sticky="W"est - sticks to left side of area
# sticky="EW" - spans to fill the entire area

# Website label and entry
website_label = Label(text="Website:", font=("Ariel", 15, "bold"), fg=RED)
website_label.grid(column=0, row=1, sticky="W")

website_entry = Entry()
# autofocuses to this field on start
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

# Email/Username label and entry
email_label = Label(text="Email/Username:", font=("Ariel", 15, "bold"), fg=RED)
email_label.grid(column=0, row=2, sticky="W")

email_entry = Entry()
email_entry.insert(index=0, string="example@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

# Password label, entry, and button
password_label = Label(text="Password:", font=("Ariel", 15, "bold"), fg=RED)
password_label.grid(column=0, row=3, sticky="W")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

password_button = Button(text="Generate", width=15, font=("Ariel", 10, "bold"), fg=RED, bg="#eeeeee", borderwidth=0,
                         command=generate_password)
password_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", font=("Ariel", 12, "bold"), fg=RED, bg="#eeeeee", borderwidth=0, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
