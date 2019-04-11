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
        super().__init__(tkRoot, f'Major Apps')

        # this is in minutes
        self.playback_time = 60

    def testCaseInfo(self):
        """ 
        Set the test case info
        This is the one that shows on the left side of the screen
        Each call of the 'makeInstructionLabel' is one line
        """
        self.makeInstructionLabel("Launch Netflix")
        self.makeInstructionLabel("Playback for 1 hour")
        self.makeInstructionLabel("Launch Amazon")
        self.makeInstructionLabel("Playback for 1 hour")
        self.makeInstructionLabel("Launch Hulu")
        self.makeInstructionLabel("Playback for 1 hour")
        self.makeInstructionLabel("Launch YouTube")
        self.makeInstructionLabel("Playback for 1 hour")

    def runThis(self):
        """
        Below is where you assemble test cases
        """

        # Launch and Playback Netflix
        self.launch_netflix()
        self.select_netflix_content()
        self.playback_netflix(self.playback_time)

        # Launch and Playback Amazon
        self.launch_amazon()
        self.select_amazon_content()
        self.playback_amazon(self.playback_time)

        # Launch and Playback Hulu
        self.launch_hulu()
        self.select_hulu_content()
        self.playback_hulu(self.playback_time)

        # Launch and Playback YouTube
        self.launch_youtube()
        self.select_youtube_content()
        self.playback_youtube(self.playback_time)



# Start the script
root = Tk()
TestScript(root).startApp()
