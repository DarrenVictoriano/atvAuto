from tkinter import *
from tkinter import ttk
import time

root = Tk()

count = 0


def counter(c=count):
    # global count
    while(c < 10):
        Label(root, text=c).pack()
        root.update()  # allow window to catch up
        time.sleep(2)
        c += 1


counter()
root.mainloop()
