from tkinter import *
from tkinter.ttk import *
from time import strftime
dub= Tk()
dub.resizable(False, False)
dub.title("Time")
label2 = Label(dub,font=("System",30),background="black",foreground="white",text="╥")
def time():
    string = strftime('%H:%M:%S %p')
    label2.config(text=string)
    label2.after(1000,time)
label2.pack()
time()
mainloop()
