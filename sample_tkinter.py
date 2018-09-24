from tkinter import *
from tkinter import ttk
import time

count = 1


def counter(c=count):
    # global count
    while(c < 10):
        ttk.Label(app, text=f'Test case {c}').grid(column=2)
        root.update()  # allow window to catch up
        time.sleep(2)
        c += 1


def repeatIt():
    for i in range(0, 5):
        counter()
        reset()
        root.update()
        time.sleep(1)
        print(i)


def reset():
    for child in app.winfo_children():
        child.destroy()


root = Tk()
root.title("Loop Tests")
app = ttk.Frame(root)
app.widget.config()
app.grid()


repeatIt()
root.mainloop()
