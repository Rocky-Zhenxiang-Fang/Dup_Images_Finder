from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class Right(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        self._set_widget()
        self.path = ""
        
    
    def _set_widget(self):
        # Image label:
        image_label = ttk.Label(text="Image Window")
        image_label.configure(anchor=CENTER)
        image_label.grid(column=0, row=0, columnspan=5)

        # Path Label:
        path_label = ttk.Label(text="")
        path_label.configure(anchor=CENTER)
        path_label.grid(column=0, row=2, columnspan=5)

        # Path Button:
        path_button = ttk.Button(text="Choose a Path", command=lambda: self._get_path(path_label))
        path_button.grid(column=0, row=1, columnspan=4, sticky=tk.W)

        # Start Button:
        start_button = ttk.Button(text="Start Hashing", command=lambda: self._start_hashing())
        start_button.grid(column=5, row=1, sticky=tk.E)


    def _get_path(self, label: ttk.Label):
        self.path = filedialog.askdirectory()
        print(self.path)
        label.grid_forget()
        label['text'] = self.path
        label.grid(column=0, row=2, columnspan=5)

    def _start_hashing(self):
        messagebox.showinfo(title='Information', message='Hello, Tkinter!')



