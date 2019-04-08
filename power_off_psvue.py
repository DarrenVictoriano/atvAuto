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
        super().__init__(tkRoot, "Power OFF PSVue")  # Update the string

        # this is in minutes
        self.playback_time = 0.1

    def testCaseInfo(self):
        """ 
        Set the test case info
        This is the one that shows on the left side of the screen
        """
        self.makeInstructionLabel("Tune to HDMI1")
        self.makeInstructionLabel("Playback HDMI1 for 1 hour")
        self.makeInstructionLabel("Do Channel Change every 10 minutes")

        self.makeInstructionLabel("Launch Netflix")
        self.makeInstructionLabel("Playback Netflix content for 1 hour")

        self.makeInstructionLabel("Launch Amazon")
        self.makeInstructionLabel("Playback Amazon content for 1 hour")

        self.makeInstructionLabel("Launch PS Vue")
        self.makeInstructionLabel("Playback PS Vue content for 1 hour")

        self.makeInstructionLabel("RC OFF TV")

    def runThis(self):
        """ Below is where you assemble test cases"""

        # launch HDMI input
        self.press_home()
        self.wait_second(5)
        self.launch_hdmi_input("HDMI1")

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

        # Launch and Playback Netflix
        self.launch_netflix()
        self.select_netflix_content()
        self.playback_netflix(self.playback_time)

        # Launch and playback Amazon
        self.launch_amazon()
        self.select_amazon_content()
        self.playback_amazon(self.playback_time)

        # Launch and Playback PSVue
        self.launch_psvue()
        self.select_psvue_content()
        self.playback_psvue(self.playback_time)

        # RC OFF the TV
        self.press_rc_key("POWER")



# Start the script
root = Tk()
Demo(root).startApp()
