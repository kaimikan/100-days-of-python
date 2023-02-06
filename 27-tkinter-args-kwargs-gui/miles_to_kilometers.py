import tkinter

window = tkinter.Tk()
window.title("miles to kilometers")
window.minsize(width=300, height=100)

conversion = "_"

# Labels

mile_text_label = tkinter.Label(text="Miles", font=('Arial', 10, "bold"))
# places element on the screen and centers it
mile_text_label.grid(column=2, row=0)

text_label = tkinter.Label(text="are equal to", font=('Arial', 10, "bold"))
# places element on the screen and centers it
text_label.grid(column=0, row=1)

conversion_label = tkinter.Label(text=f"{conversion}", font=('Arial', 15, "bold"))
# places element on the screen and centers it
conversion_label.grid(column=1, row=1)

km_text_label = tkinter.Label(text="Kilometers", font=('Arial', 10, "bold"))
# places element on the screen and centers it
km_text_label.grid(column=2, row=1)


# Button
def convert():
    conversion_label.config(text=f"{round(int(entry.get()) * 1.609344, 2)}")


button = tkinter.Button(text="Convert", command=convert)
button.grid(column=1, row=2)

# Entry
entry = tkinter.Entry(width=25)
entry.grid(column=1, row=0)

window.mainloop()
