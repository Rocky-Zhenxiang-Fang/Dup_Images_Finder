from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('My Awesome App')
        self.geometry('300x50')

        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.grid(columns=1, rows=1, rowspan=1)

        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.grid(columns=1, rows=1, rowspan=3, columnspan=3)

    def button_clicked(self):
        showinfo(title='Information', message='Hello, Tkinter!')



def main():
    app = App()

    app.mainloop()


if __name__ == '__main__':
    main()
