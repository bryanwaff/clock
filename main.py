from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Bryan waff - Clock")

def time():
    string = strftime(' %H:%M:%S - %h %y ')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 30), background = "black", foreground= "cyan")
label.pack(anchor='center')
time()

mainloop()