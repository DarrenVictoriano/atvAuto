from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import time


class SampleTkinterLoop:

    def __init__(self, master):
        # Initialize master as the Tk() instance
        self.master = master
        master.title("Sample Test")  # Change title for each test
        master.iconbitmap("img/bot_icon.ico")
        master.geometry("568x480")

        # Create frame for header and test area
        self.headerFrame = ttk.Frame(self.master)
        self.headerFrame.pack(fill=X)

        self.testCanvas = Canvas(self.master)
        self.testCanvas.pack(fill=BOTH, side=LEFT, expand=True)

        self.scrollbar = Scrollbar(self.master, command=self.testCanvas.yview)
        self.scrollbar.pack(fill=Y, side=RIGHT, expand=False)

        self.testFrame = ttk.Frame(self.testCanvas)
        self.testFrame.pack(fill=BOTH, side=LEFT, expand=True)

        # configure canvas and scrollbar
        self.testCanvas.configure(yscrollcommand=self.scrollbar.set)
        # put frame in canvas
        self.testCanvas.create_window(
            (0, 0), window=self.testFrame, width=568, anchor='nw')

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
        self.LabelLists = []

    def on_configure(self, event):
        # update scrollregion after starting 'mainloop'
        # then move scrollbar on the bottom
        self.testCanvas.configure(scrollregion=self.testCanvas.bbox('all'))
        self.testCanvas.yview_moveto(1)

    def off_configure(self, event):
        # update scrollregion after starting 'mainloop'
        # then move scrollbar on the topmost
        self.testCanvas.configure(scrollregion=self.testCanvas.bbox('all'))
        self.testCanvas.yview_moveto(0)

    def update_scrollbar(self):
        # call on_configure everytime canvas and frame change size
        self.testCanvas.bind('<Configure>', self.on_configure)
        self.testFrame.bind('<Configure>', self.on_configure)

    def reset_scrollbar(self):
        # call off_configure everytime canvas and frame change size
        self.testCanvas.bind('<Configure>', self.off_configure)
        self.testFrame.bind('<Configure>', self.off_configure)

    def bgChooser(self):
        """Background for labels"""
        if (self.bgCounter % 2) == 0:
            return str("#fff")
        return str("#e8ecf2")

    def resetLabels(self):
        """ Reset labels """
        for label in self.LabelLists:
            label.destroy()
        self.master.update()

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
        self.master.mainloop()

# Create test case inside a function --------------------------------------------------

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
        self.update_scrollbar()
        time.sleep(1)
        # revert label color to black
        x.config(foreground="#000", font=self.mainFont)
        self.LabelLists.append(x)

    def test2(self):
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
        self.update_scrollbar()
        time.sleep(1)
        # revert label color to black
        x.config(foreground="#000", font=self.mainFont)
        self.LabelLists.append(x)

    def test3(self):
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
        self.update_scrollbar()
        time.sleep(1)
        # revert label color to black
        x.config(foreground="#000", font=self.mainFont)
        self.LabelLists.append(x)

    def test4(self):
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
        self.update_scrollbar()
        time.sleep(1)
        # revert label color to black
        x.config(foreground="#000", font=self.mainFont)
        self.LabelLists.append(x)

    def test5(self):
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
        self.update_scrollbar()
        time.sleep(1)
        # revert label color to black
        x.config(foreground="#000", font=self.mainFont)
        self.LabelLists.append(x)

# End of test case inside a function --------------------------------------------------

    def repeatIt(self):
        # reset UI before starting loop
        self.resetLabels()
        # disable button while loop is running
        self.btnStart.config(state="disabled")
        self.txtLoop.config(state="disabled")
        self.labelLoop.config(text="Remaining Loop:  ")
        while self.loopCount.get() > 0:
            self.testCanvas.yview_moveto(0)
            # assemble test case below -------------------------------------
            self.test1()
            self.test2()
            self.test3()
            self.test4()
            self.test5()

            self.test1()
            self.test2()
            self.test3()
            self.test4()
            self.test5()

            self.test1()
            self.test2()
            self.test3()
            self.test4()
            self.test5()

            self.test1()
            self.test2()
            self.test3()
            self.test4()
            self.test5()

            self.test1()
            self.test2()
            self.test3()
            self.test4()
            self.test5()

            # Below are just to reset the UI ---------------------------------
            # update and reset testFrame after all function run
            self.resetLabels()
            self.reset_scrollbar()
            self.master.update()

            # pause before restarting loop
            self.loopCount.set(self.loopCount.get()-1)
            time.sleep(5)

        # re-enable button after loop is done
        self.btnStart.config(state="normal")
        self.txtLoop.config(state="normal")
        self.labelLoop.config(text="Enter Loop count: ")
        self.testCanvas.yview_moveto(0)
        # Let user know the script is done
        x = Label(
            self.testFrame, text=f'Test is done!',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)
        self.LabelLists.append(x)


root = Tk()
LoopTest = SampleTkinterLoop(root)
LoopTest.startApp()
