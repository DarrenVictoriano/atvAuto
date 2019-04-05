# Import Tkinter for GUI
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import time
import datetime
import threading
# Import the ADB_Action_Script.py it must be on the same folder
from ADB_Action_Scipt import ActionScript
# Import the RC keys and App PKGs for easy scripting
from RC_Code import SonyRCKey
from AppList import AppList
import Power_Tools as pt


class atvAuto:

    def __init__(self, tkRoot, title):
        # create an instance of the class for ATV Automation
        self.tv = ActionScript()
        self.rc = SonyRCKey()
        self.app = AppList()

        # Initialize tkRoot as the Tk() instance
        self.tkRoot = tkRoot
        self.tkRoot.title(title)  # Change title for each test
        self.tkRoot.iconbitmap("img/bot_icon.ico")
        self.tkRoot.geometry("1200x480")

        # Create frame for header
        self.headerFrame = ttk.Frame(self.tkRoot)
        self.headerFrame.pack(fill=X)

        # Create canvas and frame for Testcase Instructions
        self.sideCanvas = Canvas(self.tkRoot)
        self.sideCanvas.pack(fill=BOTH, side=LEFT)

        self.sideFrame = ttk.Frame(self.sideCanvas)
        self.sideFrame.pack(fill=BOTH, side=LEFT)

        # Create canvas for Testcase running
        self.testCanvas = Canvas(self.tkRoot)
        self.testCanvas.pack(fill=BOTH, side=LEFT, expand=True)

        # add scrollbar inside testcase canvas
        self.scrollbar = Scrollbar(self.tkRoot, command=self.testCanvas.yview)
        self.scrollbar.pack(fill=Y, side=RIGHT, expand=False)

        # Create frame for Testcase running
        self.testFrame = ttk.Frame(self.testCanvas)
        self.testFrame.pack(fill=BOTH, side=LEFT, expand=True)

        # configure canvas and scrollbar
        self.testCanvas.configure(yscrollcommand=self.scrollbar.set)

        # put sideframe in sidecanvas
        self.sideCanvas.create_window(
            (0, 0), window=self.sideFrame, anchor='nw', width=400)

        # put testFrame in testCanvas
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
        self.loopCount.set(1)
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
        """
        update scrollregion after starting 'mainloop'
        then move scrollbar on the bottom 
        """
        self.testCanvas.configure(scrollregion=self.testCanvas.bbox('all'))
        self.testCanvas.yview_moveto(1)

    def off_configure(self, event):
        """
        update scrollregion after starting 'mainloop'
        then move scrollbar on the topmost
        """
        self.testCanvas.configure(scrollregion=self.testCanvas.bbox('all'))
        self.testCanvas.yview_moveto(0)

    def update_scrollbar(self):
        """call on_configure everytime canvas and frame change size"""
        self.testCanvas.bind('<Configure>', self.on_configure)
        self.testFrame.bind('<Configure>', self.on_configure)

    def reset_scrollbar(self):
        """call off_configure everytime canvas and frame change size"""
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
    
    def makeInstructionLabel(self, textInstruction):
        """ Make label and pack it on the side for instructions"""
        Label(self.sideFrame, text=textInstruction,
              font=self.sideFont, anchor='w').pack(fill=X, padx=10)

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

    def press_home(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Press Home',
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

            self.tv.press_rc_key(self.rc.HOME)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def wait_second(self, time_wait):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Waiting {time_wait}s',
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

            self.tv.wait_in_second(time_wait)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def launch_tv_input(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launch Channel Input',
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

            self.tv.press_rc_key(self.rc.TV)
            
            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def channel_down(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Channel Down',
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

            self.tv.press_rc_key(self.rc.CHANNEL_DOWN)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")
    

    def channel_up(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Channel Up',
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

            self.tv.press_rc_key(self.rc.CHANNEL_UP)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    
    def volume_up(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Volume Up',
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

            self.tv.press_rc_key(self.rc.VOLUME_UP)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def volume_down(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Volume Down',
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

            self.tv.press_rc_key(self.rc.VOLUME_DOWN)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")
    

    def launch_stb_input(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launch HDMI1',
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

            self.tv.press_rc_key(self.rc.HDMI1)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")
    

    def launch_bdp_input(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launch HDMI2',
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

            self.tv.press_rc_key(self.rc.HDMI2)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")
    

    def press_ff(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Fast Forward',
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

            self.tv.press_rc_key(self.rc.FF)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.FF)
            self.tv.wait_in_second(2)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    
    def press_rw(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Rewind',
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

            self.tv.press_rc_key(self.rc.RW)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.RW)
            self.tv.wait_in_second(2)


            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    
    def press_play(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Playback Content for 30s',
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

            self.tv.press_rc_key(self.rc.PLAY)
            self.tv.wait_in_second(30)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def launch_netflix(self):
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launching Netflix',
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

            self.tv.press_rc_key(self.rc.HOME)
            self.tv.clear_launch_app(
            self.app.NETFLIX_PKG, self.app.NETFLIX_ACT)
            self.tv.wait_in_second(10)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def select_netflix_content(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Selecting content for playback',
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
            self.tv.wait_in_second(2)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(2)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def playback_netflix(self, pt):
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Playback Netflix',
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
            # playback time
            self.tv.wait_in_minute(pt)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def launch_amazon(self):
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launching Amazon',
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

            self.tv.press_rc_key(self.rc.HOME)
            self.tv.clear_launch_app(self.app.AMAZON_PKG, self.app.AMAZON_ACT)
            self.tv.wait_in_second(10)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def select_amazon_content(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Selecting content for playback',
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

            self.tv.press_rc_key(self.rc.DOWN)
            self.tv.wait_in_second(2)
            self.tv.press_rc_key(self.rc.DOWN)
            self.tv.wait_in_second(2)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(2)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(2)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

    def playback_amazon(self, pt):
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Playback Amazon',
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
            # playback time
            self.tv.wait_in_minute(pt)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

# End of test case inside a function --------------------------------------------------



