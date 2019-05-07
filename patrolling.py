# Import Tkinter for GUI
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

# Import necessary tools for time pause and date
import time
import datetime
import threading

# Import the ADB_Action_Script.py
# This have all the core function to control the TV
from daaf.ADB_Action_Scipt import ActionScript

# Import the RC keys and App PKGs
# This is a supporting tools for ActionScript
# It has a list of RC key code and App PKGs
from daaf.RC_Code import SonyRCKey
from daaf.AppList import AppList
import daaf.Power_Tools as pt
from daaf.atvAuto import atvAuto


class TestScript(atvAuto):

    def __init__(self, tkRoot):
        """ Initialize the UI and then Set Title Header"""
        # Update the string "Template" to your desired Title
        super().__init__(tkRoot, "Patrolling")

        # this is in minutes
        self.playback_time = 1

    def testCaseInfo(self):
        """ 
        Set the test case info
        This is the one that shows on the left side of the screen
        Each call of the 'makeInstructionLabel' is one line
        """
        self.makeInstructionLabel("Launch Channel Input")
        self.makeInstructionLabel("Do Channel Change")
        self.makeInstructionLabel("Do Volume Change")
        self.makeInstructionLabel("Launch HDMI1 with STB")
        self.makeInstructionLabel("Do Channel Change")
        self.makeInstructionLabel("Do Volume Change")
        self.makeInstructionLabel("Launch HDMI2 with BDP")
        self.makeInstructionLabel("Do Trickplay")
        self.makeInstructionLabel("Do Volume Change")

    def runThis(self):
        """
        Below is where you assemble test cases
        """

        # Home Screen
        self.press_home()
        self.wait_second(3)

        # Go to Channel Input
        self.launch_tv_input()
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

        # Go to HDMI1 Input
        self.launch_hdmi_input("HDMI1")
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

        # Go to HDMI2 Input
        self.launch_hdmi_input("HDMI2")
        self.wait_second(30)

        # Trickplay
        self.press_ff(2)
        self.press_play(10)
        self.press_rw(2)
        self.press_play(10)

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
TestScript(root).startApp()
