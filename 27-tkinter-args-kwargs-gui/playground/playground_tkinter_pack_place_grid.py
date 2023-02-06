import tkinter

# we can replace with
# from tkinter import *
# to save some typing of tkinter.Button tkinter.Label and so on
# will keep it now for clarity

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

# Pack (cannot mix with grid)
label_pack = tkinter.Label(text="PACK", font=('Arial', 25, "bold"))
# label_pack.pack(side="left", expand=False)

# Place
label_place = tkinter.Label(text="PLACE", font=('Arial', 25, "bold"))
label_place.place(x=100, y=200)

# Grid (cannot mix with pack)
label_grid = tkinter.Label(text="GRID", font=('Arial', 25, "bold"))
label_grid.grid(column=0, row=0)

# keeps window open
window.mainloop()
