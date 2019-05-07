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
        """ Initialize the UI and then Set Title Header"""
        super().__init__(tkRoot, "Power OFF Amazon")  # Update the string

        # this is in minutes
        self.playback_time = 60

    def testCaseInfo(self):
        """ 
        Set the test case info
        This is the one that shows on the left side of the screen
        """
        self.makeInstructionLabel("Launch Hulu")
        self.makeInstructionLabel("Playback Hulu content for 1 hour")
        self.makeInstructionLabel("Launch Netflix")
        self.makeInstructionLabel("Playback Netflix content for 1 hour")
        self.makeInstructionLabel("Launch Amazon")
        self.makeInstructionLabel("Playback Amazon content for 1 hour")
        self.makeInstructionLabel("RC OFF TV")

    def runThis(self):
        """ Below is where you assemble test cases"""

        # Launch and Playback Hulu
        self.launch_hulu()
        self.select_hulu_content()
        self.playback_hulu(self.playback_time)

        # Launch and Playback Netflix
        self.launch_netflix()
        self.select_netflix_content()
        self.playback_netflix(self.playback_time)

        # Launch and playback Amazon
        self.launch_amazon()
        self.select_amazon_content()
        self.playback_amazon(self.playback_time)

        # RC OFF the TV
        self.press_rc_key("POWER")


# Start the script
root = Tk()
Demo(root).startApp()
