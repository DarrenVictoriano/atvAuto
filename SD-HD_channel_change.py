# Import Tkinter for GUI
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import time
import datetime
import threading
# Import the ADB_Action_Script.py it must be on the same folder
from daaf.ADB_Action_Scipt import ActionScript
# Import the RC keys and App PKGs for easy scripting
from daaf.RC_Code import SonyRCKey
from daaf.AppList import AppList


class SampleTkinterLoop:

    def __init__(self, tkRoot):
        # create an instance of the class for ATV Automation
        self.tv = ActionScript()
        self.rc = SonyRCKey()
        self.app = AppList()

        # Initialize tkRoot as the Tk() instance
        self.tkRoot = tkRoot
        self.tkRoot.title("Major Apps Playback")  # Change title for each test
        self.tkRoot.iconbitmap("img/bot_icon.ico")
        self.tkRoot.geometry("1200x480")

        # Create frame for header and test area
        self.headerFrame = ttk.Frame(self.tkRoot)
        self.headerFrame.pack(fill=X)

        self.sideCanvas = Canvas(self.tkRoot)
        self.sideCanvas.pack(fill=BOTH, side=LEFT)

        self.sideFrame = ttk.Frame(self.sideCanvas)
        self.sideFrame.pack(fill=BOTH, side=LEFT)

        self.testCanvas = Canvas(self.tkRoot)
        self.testCanvas.pack(fill=BOTH, side=LEFT, expand=True)

        self.scrollbar = Scrollbar(self.tkRoot, command=self.testCanvas.yview)
        self.scrollbar.pack(fill=Y, side=RIGHT, expand=False)

        self.testFrame = ttk.Frame(self.testCanvas)
        self.testFrame.pack(fill=BOTH, side=LEFT, expand=True)

        # configure canvas and scrollbar
        self.testCanvas.configure(yscrollcommand=self.scrollbar.set)
        # put frame in canvas
        self.sideCanvas.create_window(
            (0, 0), window=self.sideFrame, anchor='nw', width=400)

        self.testCanvas.create_window(
            (0, 0), window=self.testFrame, anchor='nw', width=800)

        # Create a custom font
        self.mainFont = tkFont.Font(
            family="Helvetica", size=14, weight=tkFont.NORMAL)
        self.sideFont = tkFont.Font(
            family="Helvetica", size=14, weight=tkFont.NORMAL)
        self.buttonFont = tkFont.Font(
            family="Helvetica", size=10, weight=tkFont.BOLD)
        self.boldFont = tkFont.Font(
            family="Helvetica", size=14, weight=tkFont.BOLD)

        # Initialize flags for background of the labels and loop count
        self.bgCounter = 0
        self.loopCount = IntVar()
        self.loopCount.set(20000)
        self.stopLoop = False
        self.countLoopReset = 0

        # Initialize button so we can access it on any functions
        self.btnStart = Button()
        self.btnStop = Button()
        self.txtLoop = Entry()
        self.labelLoop = Label()
        self.LabelLists = []
        self.tsFormat = '%Y-%m-%d, %I:%M:%S %p'
        self.playback_time = 0.3

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
        self.tkRoot.update()

    def startApp(self):
        # Create Label for loop count
        self.labelLoop = Label(
            self.headerFrame, text=f'Enter Loop count: ',
            font=self.mainFont)
        self.labelLoop.pack(fill=X, side=LEFT)
        # Create Textbox for loop count
        self.txtLoop = Entry(self.headerFrame, font=self.mainFont,
                             textvariable=self.loopCount)
        self.txtLoop.pack(fill=X, side=LEFT)
        # Create start button
        self.btnStart = Button(self.headerFrame, text="Start Test",
                               font=self.buttonFont, command=self.start_loop, padx=55)
        self.btnStart.pack(fill=X, side=LEFT)
        # Create stop button
        self.btnStop = Button(self.headerFrame, text="Stop Test",
                              font=self.buttonFont, command=self.stopIt, padx=55)
        self.btnStop.pack(fill=X, side=LEFT)
        self.btnStop.config(state="disabled")
        # Instruction Pane ----------------
        sideLabel = Label(
            self.sideFrame, text=f'Test Case:',
            font=self.sideFont)
        sideLabel.pack(fill=X)
        # intruction below
        Label(self.sideFrame, text=f'Press Jump RC key',
              font=self.sideFont, anchor='w').pack(fill=X, padx=10)
        Label(self.sideFrame, text=f'Playback for 5 seconds',
              font=self.sideFont, anchor='w').pack(fill=X, padx=10)
        Label(self.sideFrame, text=f'Repeat..',
              font=self.sideFont, anchor='w').pack(fill=X, padx=10)
        # allow window to catch up
        self.tkRoot.update()
        self.tkRoot.mainloop()


# Function Template ---------------------------------------------------------------------

    def sample_testcase(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Sample test case',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

# Create test case inside a function --------------------------------------------------

    def jump_channel(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Jump key pressed!',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            self.tv.press_rc_key(self.rc.JUMP)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def playback_content(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Playback content',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            self.tv.wait_in_second(5)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def press_enter(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Press Enter, incase of STB network error',
                background=self.bgChooser(),
                foreground="#a5120d",
                font=self.boldFont, anchor='w')
            x.pack(fill=X)
            # add counter for BG
            self.bgCounter += 1
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
            time.sleep(1)
            # Automation Script below --------------------

            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(5)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

# End of test case inside a function --------------------------------------------------

    def stopIt(self):
        # stop main loop
        self.loopCount.set(1)
        self.stopLoop = True
        # disable stop button
        self.btnStop.config(state="disabled")
        # let user know script is stopping
        x = Label(
            self.testFrame, text=f'Stopping test..',
            background=self.bgChooser(),
            foreground="#a5120d",
            font=self.boldFont)
        x.pack(fill=X)
        # flag gor BG and labels
        self.bgCounter += 1
        self.LabelLists.append(x)
        # allow window to catch up
        self.tkRoot.update()
        self.update_scrollbar()

    def start_loop(self):
        self.stopLoop = False
        self.watch_loop()

    def watch_loop(self):
        def repeatIt():
            # reset UI and flag before starting loop
            self.resetLabels()
            self.reset_scrollbar()
            # enable stop button
            self.btnStop.config(state="normal")
            # disable button while loop is running
            self.btnStart.config(state="disabled")
            self.txtLoop.config(state="disabled")
            self.labelLoop.config(text="Remaining Loop:  ")

            while self.loopCount.get() > 0:
                # move scrollbar to bottom
                self.testCanvas.yview_moveto(0)
                # assemble test case below -------------------------------------
                self.countLoopReset += 1
                self.jump_channel()
                self.playback_content()

                # if self.countLoopReset == 1000:
                #     self.press_enter()
                #     self.countLoopReset = 1

                # Below are just to reset the UI ---------------------------------

                if not self.stopLoop:
                    print("loop not stopped so proceed")
                    # let user know script is stopping
                    x = Label(
                        self.testFrame, text=f'End of Loop',
                        background=self.bgChooser(),
                        foreground="#630984",
                        font=self.boldFont)
                    x.pack(fill=X)
                    # flag gor BG and labels
                    self.bgCounter += 1
                    self.LabelLists.append(x)
                    # allow window to catch up
                    self.tkRoot.update()
                    self.update_scrollbar()
                else:
                    print("loop has been stopped so not gonna print End of Loop")

                # pause before restarting loop
                self.loopCount.set(self.loopCount.get()-1)
                time.sleep(1)

            # disable stop button
            self.btnStop.config(state="disabled")
            # re-enable button after loop is done
            self.btnStart.config(state="normal")
            self.txtLoop.config(state="normal")
            self.labelLoop.config(text="Enter Loop count: ")
            # self.testCanvas.yview_moveto(0)
            # Let user know the script is done
            if not self.stopLoop:
                # loop did not stopped
                x = Label(
                    self.testFrame, text=f'Test is done!',
                    background=self.bgChooser(),
                    foreground="#057224",
                    font=self.boldFont)
                x.pack(fill=X)
                self.bgCounter += 1
            else:
                x = Label(
                    self.testFrame, text=f'Test stopped!',
                    background=self.bgChooser(),
                    foreground="#057224",
                    font=self.boldFont)
                x.pack(fill=X)
                self.bgCounter += 1
            self.btnStart.config(state="normal")
            self.txtLoop.config(state="normal")
            self.labelLoop.config(text="Enter Loop count: ")
            self.loopCount.set(5)
            self.LabelLists.append(x)
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
        thread = threading.Thread(target=repeatIt)
        thread.start()


root = Tk()
LoopTest = SampleTkinterLoop(root)
LoopTest.startApp()
