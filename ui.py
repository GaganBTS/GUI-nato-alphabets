from tkinter import *
from brain import *

prop = {
   "font": ("Comic Sans MS",12,"normal"),
   "bg":"white",
}
class UI():
    def __init__(self):
        self.window = Tk()
        self.window.config(padx=50, pady=50, bg="white")
        # ------------------------labels--------------------- #
        self.name_label = Label(self.window, text="Enter the name:", **prop)
        self.name_label.grid(row=1, column=0)
        self.nato_label = Label(self.window, text="NATO-alphabets are:", **prop)
        self.nato_label.grid(row=2, column=0)

        # ----------------------------entries---------------------- #
        self.name_entry = Entry(self.window, width=50)
        self.name_entry.grid(row=1, column=1, padx=10)
        self.name_entry.focus()
        self.nato_entry = Entry(self.window, width=50)
        self.nato_entry.grid(row=2, column=1, padx=10)

        # -----------------buttons---------------------------------- #
        self.enter = Button(self.window, text="ENTER", **prop, command=self.nato_alphabets)
        self.enter.grid(row=1, column=2)

        self.clear = Button(self.window, text="CLEAR", **prop, command=self.clearing)
        self.clear.grid(row=3, column=2)

        self.window.mainloop()
    def clearing(self):
        self.nato_entry.delete(0,END)
        self.name_entry.delete(0,END)
    def nato_alphabets(self):
        name = self.name_entry.get()
        output = nato_produce(name)
        self.nato_entry.insert(0,output)



