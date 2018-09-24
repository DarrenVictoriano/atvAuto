from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import time


class SampleTkinterLoop:

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

        # Initialize flags for BG and FG change
        self.bgCounter = 0
        self.fgActive = False

    def anotherLoop(self):
        # global count
        for i in range(1, 11):
            ttk.Label(
                self.app, text=f'Test case {i}',
                background=self.bgChooser(),
                foreground=self.fgChooser(),
                font=self.mainFont).pack()
            self.bgCounter += 1
            root.update()  # allow window to catch up
            time.sleep(2)

    def test1(self):
        ttk.Label(
            self.app, text=f'Test case 1',
            background=self.bgChooser(),
            foreground=self.fgChooser(),
            font=self.mainFont).pack()
        self.bgCounter += 1
        root.update()  # allow window to catch up
        time.sleep(2)

    def test2(self):
        ttk.Label(
            self.app, text=f'Test case 2',
            background=self.bgChooser(),
            foreground=self.fgChooser(),
            font=self.mainFont).pack()
        self.bgCounter += 1
        root.update()  # allow window to catch up
        time.sleep(2)

    def test3(self):
        ttk.Label(
            self.app, text=f'Test case 3',
            background=self.bgChooser(),
            foreground=self.fgChooser(),
            font=self.mainFont).pack()
        self.bgCounter += 1
        root.update()  # allow window to catch up
        time.sleep(2)

    def test4(self):
        ttk.Label(
            self.app, text=f'Test case 4',
            background=self.bgChooser(),
            foreground=self.fgChooser(),
            font=self.mainFont).pack()
        self.bgCounter += 1
        root.update()  # allow window to catch up
        time.sleep(2)

    def test5(self):
        ttk.Label(
            self.app, text=f'Test case 5',
            background=self.bgChooser(),
            foreground=self.fgChooser(),
            font=self.mainFont).pack()
        self.bgCounter += 1
        root.update()  # allow window to catch up
        time.sleep(2)

    def repeatIt(self):
        for i in range(0, 5):
            # self.anotherLoop()
            self.test1()
            self.test2()
            self.test3()
            self.test4()
            self.test5()
            self.reset()
            root.update()
            time.sleep(1)
            print(i)

    def bgChooser(self):
        if (self.bgCounter % 2) == 0:
            return str("#fff")
        return str("#ccc")

    def fgChooser(self, isActive=False):
        if isActive:
            return str("#a5120d")
        return str("#000")

    def reset(self):
        for child in self.app.winfo_children():
            child.destroy()


root = Tk()
LoopTest = SampleTkinterLoop(root)
LoopTest.repeatIt()
# LoopTest.anotherLoop()
root.mainloop()
