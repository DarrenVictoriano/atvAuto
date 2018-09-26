from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import time


class SampleTkinterLoop:

    def __init__(self, master):
        # Initialize master as the Tk() instance
        self.master = master
        master.title("Loop Tests")
        master.config(background="#e8ecf2")
        master.geometry("568x480")

        # Create main frame as app
        self.app = ttk.Frame(self.master)
        self.app.pack(fill=X)

        # Create a custom font
        self.mainFont = tkFont.Font(
            family="Helvetica", size=14, weight=tkFont.NORMAL)
        self.boldFont = tkFont.Font(
            family="Helvetica", size=14, weight=tkFont.BOLD)

        # Initialize flags for background of the labels change
        self.bgCounter = 0

    def test1(self):
        x = Label(
            self.app, text=f'Test case 1',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)
        self.bgCounter += 1
        self.master.update()  # allow window to catch up
        time.sleep(2)
        x.config(foreground="#000", font=self.mainFont)

    def test2(self):
        x = Label(
            self.app, text=f'Test case 1',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)
        self.bgCounter += 1
        self.master.update()  # allow window to catch up
        time.sleep(2)
        x.config(foreground="#000", font=self.mainFont)

    def test3(self):
        x = Label(
            self.app, text=f'Test case 1',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)
        self.bgCounter += 1
        self.master.update()  # allow window to catch up
        time.sleep(2)
        x.config(foreground="#000", font=self.mainFont)

    def test4(self):
        x = Label(
            self.app, text=f'Test case 1',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)
        self.bgCounter += 1
        self.master.update()  # allow window to catch up
        time.sleep(2)
        x.config(foreground="#000", font=self.mainFont)

    def test5(self):
        x = Label(
            self.app, text=f'Test case 1',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)
        self.bgCounter += 1
        self.master.update()  # allow window to catch up
        time.sleep(2)
        x.config(foreground="#000", font=self.mainFont)

    def repeatIt(self):
        for i in range(0, 5):
            # self.anotherLoop()
            self.test1()
            self.test2()
            self.test3()
            self.test4()
            self.test5()
            self.reset()
            self.master.update()
            time.sleep(1)
            print(i)

    def bgChooser(self):
        if (self.bgCounter % 2) == 0:
            return str("#fff")
        return str("#e8ecf2")

    def reset(self):
        for child in self.app.winfo_children():
            child.destroy()


root = Tk()
LoopTest = SampleTkinterLoop(root)
LoopTest.repeatIt()
root.mainloop()
