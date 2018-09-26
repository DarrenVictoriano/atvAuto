from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import time


class SampleTkinterLoop:
    count = 1

    def __init__(self, master):
        # Initialize master as the Tk() instance
        self.master = master
        master.title("Loop Tests")
        master.geometry("768x480")

        # Create main frame as app
        self.app = ttk.Frame(root)
        self.app.pack(fill="both", expand=True)

        # Create a custom font
        self.mainFont = tkFont.Font(family="Helvetica", size=12)

    def counter(self, c=count):
        # global count
        while c < 10:
            ttk.Label(
                self.app, text=f'Test case {c}', font=self.mainFont).pack()
            root.update()  # allow window to catch up
            time.sleep(2)
            c += 1

    def repeatIt(self):
        for i in range(0, 5):
            # self.counter()
            self.anotherLoop()
            self.reset()
            root.update()
            time.sleep(1)
            print(i)

    def reset(self):
        for child in self.app.winfo_children():
            child.destroy()

    def anotherLoop(self):
        # global count
        for i in range(1, 11):
            ttk.Label(
                self.app, text=f'Test case {i}', font=self.mainFont).pack()
            root.update()  # allow window to catch up
            time.sleep(2)


root = Tk()
LoopTest = SampleTkinterLoop(root)
LoopTest.repeatIt()
# LoopTest.anotherLoop()
root.mainloop()
