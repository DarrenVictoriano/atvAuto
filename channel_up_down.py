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

    def __init__(self, tkRoot, hdmi):
        """ Initialize the UI and then Set Title Header"""
        # Update the string "Template" to your desired Title
        super().__init__(tkRoot, f'Channel Up/Down HMDI{hdmi}')

        # this is in minutes
        self.playback_time = 1
        self.hdmiTest = hdmi

    def testCaseInfo(self):
        """ 
        Set the test case info
        This is the one that shows on the left side of the screen
        Each call of the 'makeInstructionLabel' is one line
        """
        self.makeInstructionLabel(f'Tune to HDMI{hdmi} for 1 hour')
        self.makeInstructionLabel("Channel Change every 10 minutes")

    def runThis(self):
        """
        Below is where you assemble test cases
        """

        # launch HDMI input
        self.press_home()
        self.wait_second(5)
        self.launch_hdmi_input(f'HDMI{self.hdmiTest}')
        self.wait_second(15)

        # Do Channel Up every 10 minutes for 1 hour
        for i in range(1, 4):
            print(f'loop count {i}')
            self.channel_up()
            self.wait_minute(10)

        # Do Channel Down every 10 minutes for 1 hour
        for i in range(1, 4):
            print(f'loop count {i}')
            self.channel_down()
            self.wait_minute(10)


# Select HDMI
hdmi = input("Enter which HDMI you want to test (1, 2, 3 or 4): ")

# Start the script
root = Tk()
TestScript(root, hdmi).startApp()
