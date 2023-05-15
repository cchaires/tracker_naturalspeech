from tkinter import *

THEME_COLOR = "#229954"


class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tracker Natural Speech")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(345, 490)
        self.window.mainloop()
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1)
