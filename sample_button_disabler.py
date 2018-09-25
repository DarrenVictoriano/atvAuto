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
        self.footerFrame = ttk.Frame(self.master)
        self.footerFrame.pack(fill=X, side="bottom")

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

        # Initialize button so we can access it on any functions
        self.btnStart = Button()
        self.txtLoop = Entry()
        self.labelLoop = Label()

    def test1(self):
        # Create label
        x = Label(
            self.testFrame, text=f'Test case 1',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)
        # add counter for BG
        self.bgCounter += 1
        # allow window to catch up
        self.master.update()
        time.sleep(2)
        # revert label color to black
        x.config(foreground="#000", font=self.mainFont)

    def test2(self):
        # Create label
        x = Label(
            self.testFrame, text=f'Test case 2',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)
        # add counter for BG
        self.bgCounter += 1
        # allow window to catch up
        self.master.update()
        time.sleep(2)
        # revert label color to black
        x.config(foreground="#000", font=self.mainFont)

    def test3(self):
        # Create label
        x = Label(
            self.testFrame, text=f'Test case 3',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)
        # add counter for BG
        self.bgCounter += 1
        # allow window to catch up
        self.master.update()
        time.sleep(2)
        # revert label color to black
        x.config(foreground="#000", font=self.mainFont)

    def test4(self):
        # Create label
        x = Label(
            self.testFrame, text=f'Test case 4',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)
        # add counter for BG
        self.bgCounter += 1
        # allow window to catch up
        self.master.update()
        time.sleep(2)
        # revert label color to black
        x.config(foreground="#000", font=self.mainFont)

    def test5(self):
        # Create label
        x = Label(
            self.testFrame, text=f'Test case 5',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)
        # add counter for BG
        self.bgCounter += 1
        # allow window to catch up
        self.master.update()
        time.sleep(2)
        # revert label color to black
        x.config(foreground="#000", font=self.mainFont)

    def repeatIt(self):
        # reset UI before starting loop
        self.resetTestFrame()
        # disable button while loop is running
        self.btnStart.config(state="disabled")
        self.txtLoop.config(state="disabled")
        self.labelLoop.config(text="Remaining Loop:  ")
        while self.loopCount.get() > 0:
            # for i in range(0, self.loopCount.get()):
            # assemble test case below
            self.test1()
            self.test2()
            self.test3()
            self.test4()
            self.test5()

            # update and reset testFrame after all function run
            self.resetTestFrame()
            self.master.update()

            # pause before restarting loop
            self.loopCount.set(self.loopCount.get()-1)
            time.sleep(1)

        # re-enable button after loop is done
        self.btnStart.config(state="normal")
        self.txtLoop.config(state="normal")
        self.labelLoop.config(text="Enter Loop count: ")
        # Let user know the script is done
        x = Label(
            self.testFrame, text=f'Test is done!',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)

    def bgChooser(self):
        if (self.bgCounter % 2) == 0:
            return str("#fff")
        return str("#e8ecf2")

    def resetTestFrame(self):
        for child in self.testFrame.winfo_children():
            child.destroy()

    def startApp(self):
        # Create Label
        self.labelLoop = Label(
            self.headerFrame, text=f'Enter Loop count: ',
            font=self.mainFont)
        self.labelLoop.pack(fill=X, side=LEFT)
        # Create Textbox
        self.txtLoop = Entry(self.headerFrame, font=self.mainFont,
                             textvariable=self.loopCount)
        self.txtLoop.pack(fill=X, side=LEFT)
        # Create Button
        self.btnStart = Button(self.headerFrame, text="Start Test",
                               font=self.buttonFont, command=self.repeatIt, padx=55)
        self.btnStart.pack(fill=X, side=LEFT)
        # allow window to catch up
        self.master.update()


root = Tk()
LoopTest = SampleTkinterLoop(root)
LoopTest.startApp()
root.mainloop()
