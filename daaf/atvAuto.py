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

        # Create canvas Testcase Instructions
        self.sideCanvas = Canvas(self.tkRoot)
        self.sideCanvas.pack(fill=BOTH, side=LEFT)

        # Create Frame for Testcase Instructions
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
        self.deviceID = StringVar()
        self.stopLoop = False
        self.countLoopReset = 0

        # Initialize button so we can access it on any functions
        self.btnStart = Button()
        self.btnStop = Button()
        self.txtLoop = Entry()
        self.labelLoop = Label()
        self.txtDeviceID = Entry()
        self.labelDeviceID = Label()
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
        # Set DeviceID to the ATV MainScript
        self.tv.deviceID = self.deviceID.get()

        self.stopLoop = False
        self.watch_loop()
    
    def watch_loop(self):
        # Double threaded function that allows to stop the loop mid execution
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

                # Run the test cases
                self.runThis()

                # Below are just to reset the UI
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
            self.loopCount.set(1)
            self.LabelLists.append(x)
            # allow window to catch up
            self.tkRoot.update()
            self.update_scrollbar()
        thread = threading.Thread(target=repeatIt)
        thread.start()

    def startApp(self):
        # Create Label for loop count
        self.labelLoop = Label(
            self.headerFrame, text=f'Enter Loop count: ',
            font=self.mainFont)
        self.labelLoop.pack(fill=X, side=LEFT)

        # Create Textbox for loop count
        self.txtLoop = Entry(self.headerFrame, font=self.mainFont,
                             textvariable=self.loopCount, width=8)
        self.txtLoop.pack(fill=X, side=LEFT)

        # Create Label for DeviceID
        self.labelDeviceID = Label(
            self.headerFrame, text=f'    Enter ADB ID or TVs IP: ',
            font=self.mainFont)
        self.labelDeviceID.pack(fill=X, side=LEFT)

        # Create Textbox for DeviceID
        self.txtDeviceID = Entry(self.headerFrame, font=self.mainFont,
                             textvariable=self.deviceID)
        self.txtDeviceID.pack(fill=X, side=LEFT)

        # Create start button
        self.btnStart = Button(self.headerFrame, text="Start Test",
                               font=self.buttonFont, command=self.start_loop, padx=55)
        self.btnStart.pack(fill=X, side=LEFT)

        # Create stop button
        self.btnStop = Button(self.headerFrame, text="Stop Test",
                              font=self.buttonFont, command=self.stopIt, padx=55)
        self.btnStop.pack(fill=X, side=LEFT)
        self.btnStop.config(state="disabled")

        # Initialize Instruction Pane ----------------
        sideLabel = Label(
            self.sideFrame, text=f'Test Case:',
            font=self.sideFont)
        sideLabel.pack(fill=X)

        # Change intruction below based on the testcase
        self.testCaseInfo()

        # Allow window to refresh
        self.tkRoot.update()
        self.tkRoot.mainloop()

    def testCaseInfo(self):
        """ This will be overriden by the subclass"""
        print("Override method..")
    
    def runThis(self):
        """ This will be overriden by the subclass"""
        print("Override method..")

# Create test case inside a function --------------------------------------------------

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

    
    def wait_minute(self, time_wait):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Waiting {time_wait} minute/s',
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

            self.tv.wait_in_minute(time_wait)

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
    

    def launch_hdmi_input(self, hdmi):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launch {hdmi.upper()}',
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

            self.tv.press_rc_key(getattr(self.rc, hdmi.upper()))

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")
    

    def press_rc_key(self, key_code):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Press {key_code.upper()}',
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

            self.tv.press_rc_key(getattr(self.rc, key_code.upper()))

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def press_ff(self, playTime):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Fast Forward for {pt}s',
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
            self.tv.wait_in_second(playTime)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def press_rw(self, playTime):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Rewind for {pt}s',
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
            self.tv.wait_in_second(playTime)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def press_play(self, playTime):
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
            self.tv.wait_in_second(playTime)

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
            self.tv.wait_in_second(3)

            self.tv.press_rc_key(self.rc.ENTER)
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


    def playback_netflix(self, playtime):
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
            self.tv.wait_in_minute(playtime)

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


    def playback_amazon(self, playtime):
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
            self.tv.wait_in_minute(playtime)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def launch_hulu(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launching Hulu',
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
            self.tv.wait_in_second(1)
            self.tv.clear_launch_app(self.app.HULU_PKG, self.app.HULU_ACT)
            self.tv.wait_in_second(10)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def select_hulu_content(self):
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
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(1)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def playback_hulu(self, playtime):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Playback Hulu',
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

            self.tv.wait_in_minute(playtime)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def launch_vudu(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launching Vudu',
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
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(10)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def select_vudu_content(self):
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
            
            self.tv.press_rc_key(self.rc.RIGHT)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.RIGHT)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.DOWN)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(1)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def playback_vudu(self, playtime):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Playback Vudu',
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

            self.tv.wait_in_minute(playtime)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def launch_youtube(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launching YouTube',
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
            self.tv.wait_in_second(1)
            self.tv.force_stop_app(self.app.YOUTUBE_PKG)
            self.tv.wait_in_second(1)
            self.tv.launch_app(self.app.YOUTUBE_PKG)
            self.tv.wait_in_second(10)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def select_youtube_content(self):
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

            self.tv.press_rc_key(self.rc.RIGHT)
            self.tv.wait_in_second(1)
            self.tv.press_rc_key(self.rc.ENTER)
            self.tv.wait_in_second(1)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def playback_youtube(self, playtime):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Playback YouTube',
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

            self.tv.wait_in_minute(playtime)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def launch_psvue(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launch PSVue',
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
            self.tv.wait_in_second(1)

            self.tv.clear_launch_app(
            self.app.PSVUE_PKG, self.app.PSVUE_ACT)

            self.tv.wait_in_second(10)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def select_psvue_content(self):
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
            self.tv.wait_in_second(1)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def playback_psvue(self, playtime):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Playback PSVue',
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

            self.tv.wait_in_minute(playtime)
            
            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def launch_parental_lock(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Launch Parental Lock',
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
            self.tv.wait_in_second(1)

            self.tv.clear_launch_app(
            self.app.PARENTAL_LOCK_PKG, self.app.PARENTAL_LOCK_ACT)
            self.tv.wait_in_second(2)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def enter_parental_pass(self):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Entering PIN',
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
            
            # Enter Pin
            for i in range(0, 4):
                print(f'Press Enter {i}')
                self.tv.press_rc_key(self.rc.ENTER)

            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")


    def lock_unlock_hdmi(self, hdmi):
        # each test case 1st check for the stop button flag
        if not self.stopLoop:
            # get time
            ts = datetime.datetime.now().strftime(self.tsFormat)
            # Create label
            x = Label(
                self.testFrame, text=f'{ts} - Lock/Unlock HDMI{hdmi}',
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
            
            # select 'External Input Block'
            for i in range(0, 3):
                self.tv.press_rc_key(self.rc.DOWN)

            self.tv.press_rc_key(self.rc.ENTER)

            if hdmi == '1':
                self.tv.press_rc_key(self.rc.ENTER)
            elif hdmi == '2':
                self.tv.press_rc_key(self.rc.DOWN)
                self.tv.press_rc_key(self.rc.ENTER)
            elif hdmi == '3':
                self.tv.press_rc_key(self.rc.DOWN)
                self.tv.press_rc_key(self.rc.DOWN)
                self.tv.press_rc_key(self.rc.ENTER)
            elif hdmi == '4':
                self.tv.press_rc_key(self.rc.DOWN)
                self.tv.press_rc_key(self.rc.DOWN)
                self.tv.press_rc_key(self.rc.DOWN)
                self.tv.press_rc_key(self.rc.ENTER)


            # Automation Script above --------------------

            # revert label color to black
            x.config(foreground="#000", font=self.mainFont)
            self.LabelLists.append(x)
        else:
            print("stopping test")

# End of test case inside a function --------------------------------------------------
