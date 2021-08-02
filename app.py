from tkinter import *
import tkinter as tk
from tkinter import ttk
import right

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        right_frame = right.Right(self)
        right_frame.grid(column=0, row=0)



if __name__ == '__main__':
    app = App()
    # app.resizable(0, 0)
    app.mainloop()