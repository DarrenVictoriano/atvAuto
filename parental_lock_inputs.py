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
        super().__init__(tkRoot, "Parental Lock Inputs")

        # this is in minutes
        self.playback_time = 1
        self.hdmi_to_test = hdmi

    def testCaseInfo(self):
        """ 
        Set the test case info
        This is the one that shows on the left side of the screen
        Each call of the 'makeInstructionLabel' is one line
        """
        self.makeInstructionLabel("Launch Parental Lock Activity")
        self.makeInstructionLabel("Input PIN Code")
        self.makeInstructionLabel(f'Lock HDMI{self.hdmi_to_test}')
        self.makeInstructionLabel(
            f'Tune to verify HDMI{self.hdmi_to_test} is locked')

    def runThis(self):
        """
        Below is where you assemble test cases
        """

        # Launch Parental Lock
        self.launch_parental_lock()
        self.enter_parental_pass()

        # Lock or Unlock HDMI
        self.lock_unlock_hdmi(self.hdmi_to_test)
        self.wait_second(2)

        # Tune to the locked HDMI
        self.press_home()
        self.wait_second(2)
        self.launch_hdmi_input(f'HDMI{self.hdmi_to_test}')
        self.wait_second(3)



# Select HDMI
hdmi = input("Enter which HDMI you want to test (1, 2, 3 or 4): ")

# Start the script
root = Tk()
TestScript(root, hdmi).startApp()
