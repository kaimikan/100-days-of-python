from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#f8a89d"
RED = "#f1583f"
GREEN = "#379b46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 3
LONG_BREAK_MIN = 10
session_number = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global session_number
    global timer
    window.after_cancel(timer)

    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_time, text="00:00")
    checkmark_label.config(text="")

    session_number = 1


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global session_number
    work_seconds = WORK_MIN * 1
    short_break_seconds = SHORT_BREAK_MIN * 1
    long_break_seconds = LONG_BREAK_MIN * 1

    if session_number % 2 == 1:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_seconds)
    elif session_number % 8 == 0:
        title_label.config(text="BREAK", fg=RED)
        count_down(long_break_seconds)
    else:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes_in_time = math.floor(count / 60)
    seconds_in_time = count % 60
    if minutes_in_time >= 10:
        minutes_string = f"{minutes_in_time}"
    else:
        minutes_string = f"0{minutes_in_time}"

    if seconds_in_time >= 10:
        seconds_string = f"{seconds_in_time}"
    else:
        seconds_string = f"0{seconds_in_time}"

    # dynamic typing python thread (look for strongly dynamically typed):
    # https://stackoverflow.com/questions/11328920/is-python-strongly-typed

    second_in_milliseconds = 1000
    canvas.itemconfig(timer_time, text=f"{minutes_string}:{seconds_string}")
    # a much more concise solution is
    # canvas.itemconfig(timer_time, text=f"{minutes_in_time:02}:{seconds_in_time:02}")
    print(count)
    if count > 0:
        timer = window.after(second_in_milliseconds, count_down, count - 1)
    elif count == 0:
        global session_number
        session_number += 1
        # using some list comprehension
        checkmarks = ["✓" for session in range(1, session_number) if session % 2 == 1]
        checkmark_string = ""
        for checkmark in checkmarks:
            checkmark_string += checkmark
        checkmark_label.config(text=f"{checkmark_string}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Labels
title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

checkmark_label = Label(text="", font=(FONT_NAME, 25, "bold"), fg=RED, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

# Buttons
start_button = Button(text="Start", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW, borderwidth=0,
                      command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 20, "bold"), fg=RED, bg=YELLOW, borderwidth=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# we base width and height on the tomato image dimensions
image_height = 224
image_width = 200
canvas = Canvas(width=image_width, height=image_height, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(image_width / 2, image_height / 2, image=tomato_image)
timer_time = canvas.create_text(image_width / 2, image_height / 2 + 20, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
