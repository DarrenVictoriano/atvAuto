from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import time


class SampleTkinterLoop:

    def __init__(self, master):
        # Initialize master as the Tk() instance
        self.master = master
        master.title("Sample Test")
        master.iconbitmap("img/bot_icon.ico")
        master.geometry("568x480")

        # Create frame for header and test area
        self.headerFrame = ttk.Frame(self.master)
        self.headerFrame.pack(fill=X)
        self.testFrame = ttk.Frame(self.master)
        self.testFrame.pack(fill=X)

        # Create a custom font
        self.mainFont = tkFont.Font(
            family="Helvetica", size=14, weight=tkFont.NORMAL)
        self.buttonFont = tkFont.Font(
            family="Helvetica", size=10, weight=tkFont.BOLD)
        self.boldFont = tkFont.Font(
            family="Helvetica", size=14, weight=tkFont.BOLD)

        # Initialize flags for background of the labels and loop count
        self.bgCounter = 0
        self.loopCount = IntVar()
        self.loopCount.set(5)

    def test1(self):
        x = Label(
            self.testFrame, text=f'Test case 1',
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
            self.testFrame, text=f'Test case 2',
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
            self.testFrame, text=f'Test case 3',
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
            self.testFrame, text=f'Test case 4',
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
            self.testFrame, text=f'Test case 5',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)
        self.bgCounter += 1
        self.master.update()  # allow window to catch up
        time.sleep(2)
        x.config(foreground="#000", font=self.mainFont)

    def repeatIt(self):
        for i in range(0, self.loopCount.get()):
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
        for child in self.testFrame.winfo_children():
            child.destroy()

    def startApp(self):
        # Create Label
        x = Label(
            self.headerFrame, text=f'Enter Loop count: ',
            font=self.mainFont)
        x.pack(fill=X, side=LEFT)
        # Create Textbox
        txtLoop = Entry(self.headerFrame, font=self.mainFont,
                        textvariable=self.loopCount)
        txtLoop.pack(fill=X, side=LEFT)
        # Create Button
        b = Button(self.headerFrame, text="Start Test",
                   font=self.buttonFont, command=self.repeatIt, padx=55)
        b.pack(fill=X, side=LEFT)
        # allow window to catch up
        self.master.update()


root = Tk()
LoopTest = SampleTkinterLoop(root)
LoopTest.startApp()
root.mainloop()
