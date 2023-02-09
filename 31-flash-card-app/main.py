from tkinter import Button, PhotoImage, Tk, Canvas, Label
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Calibri"

# read words from csv and transfer to dict
# notice orient='records'
# creates a list of dictionaries: [{column -> value}, … , {column -> value}]

try:
    words_csv = pandas.read_csv("./data/french_words_to_learn.csv")
# if the file does not exist or if the file exists but is empty
except (FileNotFoundError, pandas.errors.EmptyDataError):
    words_csv = pandas.read_csv("./data/french_words_static_storage.csv")
finally:
    # in the case where we can read the french_words_to_learn, but it contains 0 entries
    if len(words_csv) == 0:
        words_csv = pandas.read_csv("./data/french_words_static_storage.csv")

words = words_csv.to_dict(orient="records")

current_word = {}

TIME_FOR_CHANGE = 3
timer = None


def display_random_word():
    global words, current_word
    right_button["state"] = "disable"
    wrong_button["state"] = "disable"

    canvas.itemconfig(flash_card, image=flash_card_front_image)

    if len(words) == 0:
        canvas.itemconfig(language_text, text=f"No More Words", fill="black")
        canvas.itemconfig(word_text, text=f"Good Job!", fill="black")
    else:
        current_word = words[random.randint(0, len(words) - 1)]
        french = current_word["French"]

        canvas.itemconfig(language_text, text=f"French", fill="black")
        canvas.itemconfig(word_text, text=f"{french}", fill="black")
        # canvas.itemconfig(flash_card, image=flash_card_front_image)

        # we can also put the timer here and call the flip_card method after time_for_change seconds
        flip_card()


# non-default parameters should be first in the method
def flip_card(seconds_to_change=TIME_FOR_CHANGE):
    global timer, current_word
    english = current_word["English"]
    # flip card after TIME_FOR_CHANGE seconds
    if seconds_to_change > 0:
        # since we call this recursively
        # each increment is 1 second or 1000 milliseconds
        timer = window.after(1000, flip_card, seconds_to_change - 1)
    else:
        canvas.itemconfig(language_text, text=f"English", fill="white")
        canvas.itemconfig(word_text, text=f"{english}", fill="white")
        canvas.itemconfig(flash_card, image=flash_card_back_image)
        window.after_cancel(timer)
        right_button["state"] = "normal"
        wrong_button["state"] = "normal"


def known_word():
    # since the user knows the word we remove it from the showable words list
    words.remove(current_word)
    words_to_df = pandas.DataFrame(words)
    # index=False removes the numbers which pandas automatically puts in the csv
    words_to_df.to_csv("./data/french_words_to_learn.csv", index=False)

    display_random_word()


def unknown_word():
    # skip onto next word
    display_random_word()


window = Tk()
window.title("Flash Cards - French/English")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flash_card_width = 800
flash_card_height = 526

canvas = Canvas(width=flash_card_width, height=flash_card_height, highlightthickness=0, background=BACKGROUND_COLOR)

# order of elements matters if it's image last and text first, the text remains behind
flash_card_front_image = PhotoImage(file="./images/card_front.png")
flash_card_back_image = PhotoImage(file="./images/card_back.png")
flash_card = canvas.create_image(flash_card_width / 2, flash_card_height / 2, image=flash_card_front_image)

language_text = canvas.create_text(flash_card_width / 2, flash_card_height / 2 - 90, text="French",
                                   font=(FONT_NAME, 25, "italic"))
word_text = canvas.create_text(flash_card_width / 2, flash_card_height / 2, text="word",
                               font=(FONT_NAME, 35, "bold"))
canvas.grid(column=0, row=0, columnspan=2, sticky="EW")

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=unknown_word)
wrong_button["state"] = "disable"
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=known_word)
right_button["state"] = "disable"
right_button.grid(column=1, row=1)

display_random_word()

window.mainloop()
