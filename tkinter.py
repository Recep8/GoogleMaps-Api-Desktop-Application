import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Distance and duration between two location')
        self.geometry("600x800")

        self.address1_var = tk.StringVar()
        self.address2_var = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):

        padding = {'padx':5,'pady': 5}

        #Label
        ttk.Label(self, text='First Address:').grid(column=0, row=0, **padding)
        ttk.Label(self, text='Second Address:').grid(column=0, row=1, **padding)

        #Entry
        name_entry = ttk.Entry(self, textvariable=self.address1_var)
        name_entry2 = ttk.Entry(self, textvariable=self.address2_var)
        name_entry.grid(column=1, row=0, **padding)
        name_entry2.grid(column=1, row=1, **padding)
        name_entry.focus()
        name_entry2.focus()



        #Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=2, row=1, **padding)

        #Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=2, columnspan=3, **padding)
        self.address1_var.get()
        self.address2_var.get()

    def submit(self):
        self.output_label.config(text=self.address1_var.get()+self.address2_var.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()
