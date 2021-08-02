from tkinter import *
import tkinter as tk
from tkinter import ttk

class ImageCheckBox(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.state = IntVar()   # 0 for delete, 1 for save
        self.state.set(1)
        self.image_label = ttk.Label(self, text="Image")
        self.image_name = ttk.Label(self, text="Name")
        self.delete_radio = ttk.Radiobutton(self,text="Delete", variable=self.state, value=0, command=self._test_radio)
        self.save_radio = ttk.Radiobutton(self,text="Save", variable=self.state, value=1, command=self._test_radio)
        self._pack_widget()

    def _pack_widget(self):
        self.image_name.grid(column=0, row=0, columnspan=2, sticky=tk.W)
        self.image_label.grid(column=2, row=0, rowspan=2)
        self.save_radio.grid(column=0, row=1)
        self.delete_radio.grid(column=1, row=1)
    
    def _test_radio(self):
        print(self.state.get())


if __name__ == "__main__":
    app = tk.Tk()
    for i in range(5):
        image_checkbox = ImageCheckBox(app)
        image_checkbox.pack()
    app.mainloop()

