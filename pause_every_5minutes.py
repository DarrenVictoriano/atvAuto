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
        super().__init__(tkRoot, "Netflix Pause - 5min")

        # this is in minutes
        self.playback_time = 1
        # set loopCount default value
        self.loopCount.set(50000)

    def testCaseInfo(self):
        """ 
        Set the test case info
        This is the one that shows on the left side of the screen
        Each call of the 'makeInstructionLabel' is one line
        """
        self.makeInstructionLabel("Before Starting the Script:")
        self.makeInstructionLabel("Launch any app")
        self.makeInstructionLabel("Select and playback content")
        self.makeInstructionLabel(" ----------------------------------")
        self.makeInstructionLabel("What the script does:")
        self.makeInstructionLabel("Press Pause every 5 minutes")

    def runThis(self):
        """
        Below is where you assemble test cases
        """
        self.wait_minute(5)
        self.press_rc_key("PAUSE")



# Start the script
root = Tk()
TestScript(root).startApp()
