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
        super().__init__(tkRoot, "Power OFF HDMI")  # Update the string

    def testCaseInfo(self):
        """ Update what the script does"""
        self.makeInstructionLabel("Launch HDMI1 with STB for 1 hour")
        self.makeInstructionLabel("Do Channel change every 10 minutes")
        self.makeInstructionLabel("Launch Netflix")
        self.makeInstructionLabel("Playback Netflix Content for 1 hour")
        self.makeInstructionLabel("Launch Amazon")
        self.makeInstructionLabel("Playback Amazon Content for 1 hour")
        self.makeInstructionLabel("Launch HDMI1 with STB for 1 hour")
        self.makeInstructionLabel("Power OFF TV")

    def runThis(self):
        """ Below is where you assemble test cases"""

        # launch HDMI input
        self.press_home()
        self.wait_second(5)
        self.launch_hdmi_input("HDMI1")

        # Do Channel Up every 10 minutes for 1 hour
        for i in range(1, 4):
            self.channel_up()
            self.wait_minute(self.playback_time)
        # Do Channel Down every 10 minutes for 1 hour
        for i in range(1, 4):
            self.channel_down()
            self.wait_minute(self.playback_time)

        # Launch and playback Netflix
        self.launch_netflix()
        self.select_netflix_content()
        self.playback_netflix(self.playback_time)

        # Launch and Playback Amazon
        self.launch_amazon()
        self.select_amazon_content()
        self.playback_amazon(self.playback_time)

        # launch HDMI input
        self.press_home()
        self.wait_second(5)
        self.launch_hdmi_input("HDMI1")

        # Do Channel Up every 10 minutes for 1 hour
        for i in range(1, 4):
            self.channel_up()
            self.wait_minute(self.playback_time)
        # Do Channel Down every 10 minutes for 1 hour
        for i in range(1, 4):
            self.channel_down()
            self.wait_minute(self.playback_time)

        self.press_rc_key("POWER")


# Start the script
root = Tk()
Demo(root).startApp()
