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
import daaf.Power_Tools as pt
from daaf.atvAuto import atvAuto


class Demo(atvAuto):

    def __init__(self, tkRoot):
        super().__init__(tkRoot, "Demo")

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

        # Initialize Instruction Pane ----------------
        sideLabel = Label(
            self.sideFrame, text=f'Test Case:',
            font=self.sideFont)
        sideLabel.pack(fill=X)

        # intruction below
        self.makeInstructionLabel("Launch HDMI1 with STB")
        self.makeInstructionLabel("Do Channel change")
        self.makeInstructionLabel("Do Volume change")
        self.makeInstructionLabel("Launch Netflix")
        self.makeInstructionLabel("Playback Netflix Content")
        self.makeInstructionLabel("Do Trickplay")
        self.makeInstructionLabel("Do volume change")
        self.makeInstructionLabel("Launch Amazon")
        self.makeInstructionLabel("Playback Amazon Content")
        self.makeInstructionLabel("Do Trickplay")
        self.makeInstructionLabel("Do volume change")

        # allow window to catch up
        self.tkRoot.update()
        self.tkRoot.mainloop()

    # this need to go to the subclass
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

# assemble test case below -------------------------------------
    def runThis(self):
        """ This is where you assemble test cases"""
        # Home Screen
        self.press_home()
        self.wait_second(3)

        # Go to HDMI1 Input
        self.launch_stb_input()
        self.wait_second(5)

        # channel Down 3 times
        for i in range(1, 4):
            self.channel_down()
            self.wait_second(3)
            print(f'CH Down press count: {i}')

        # Channel Up 3 times
        for i in range(1, 4):
            self.channel_up()
            self.wait_second(3)
            print(f'CH Up press count: {i}')

        # Volume Up 3 times
        for i in range(1, 4):
            self.volume_up()
            print(f'VOL Up press count: {i}')

        # Volume Down 3 times
        for i in range(1, 4):
            self.volume_down()
            print(f'VOL Down press count: {i}')

        # Launch and playback netflix
        self.launch_netflix()
        self.select_netflix_content()
        self.playback_netflix(self.playback_time)

        # Trickplay
        self.press_ff()
        self.press_play()
        self.press_rw()
        self.press_play()

        # Volume Up 3 times
        for i in range(1, 4):
            self.volume_up()
            print(f'VOL Up press count: {i}')

        # Volume Down 3 times
        for i in range(1, 4):
            self.volume_down()
            print(f'VOL Down press count: {i}')

        # Launch Amazon and Play content
        self.launch_amazon()
        self.select_amazon_content()
        self.playback_amazon(self.playback_time)

        # Trickplay
        self.press_ff()
        self.press_play()
        self.press_rw()
        self.press_play()

        # Volume Up 3 times
        for i in range(1, 4):
            self.volume_up()
            print(f'VOL Up press count: {i}')

        # Volume Down 3 times
        for i in range(1, 4):
            self.volume_down()
            print(f'VOL Down press count: {i}')


# Start the script
root = Tk()
Demo(root).startApp()
