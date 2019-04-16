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

    def __init__(self, tkRoot, hdmi, deviceType):
        """ Initialize the UI and then Set Title Header"""
        # Update the string "Template" to your desired Title
        super().__init__(tkRoot, f'IOP on HDMI{hdmi}')

        # this is in minutes
        self.playback_time = 1
        self.hdmi_test = hdmi
        self.device_type = deviceType

    def testCaseInfo(self):
        """ 
        Set the test case info
        This is the one that shows on the left side of the screen
        Each call of the 'makeInstructionLabel' is one line
        """
        deviceTitle = "Media Box"

        if self.device_type == '1':
            deviceTitle = "STB"

        self.makeInstructionLabel("Do RC Power Cycle 3 times")
        self.makeInstructionLabel("Do Input Change 3 times")
        if deviceTitle == "STB":
            self.makeInstructionLabel("Do Channel Change 3 times")
        else:
            self.makeInstructionLabel("Do Trickplay 3 times")
        self.makeInstructionLabel("Press TV RC Keys")
        self.makeInstructionLabel("Then Press all on-screen buttons")
        self.makeInstructionLabel("Press Guide RC Keys")
        self.makeInstructionLabel("Then Select any channel")
        self.makeInstructionLabel("Launch and Playback Netflix")
        self.makeInstructionLabel(f'Tune back to HDMI{self.hdmi_test}')
        self.makeInstructionLabel("Launch and Playback Amazon")
        self.makeInstructionLabel(f'Tune back to HDMI{self.hdmi_test}')
        self.makeInstructionLabel("Launch and Playback Hulu")
        self.makeInstructionLabel(f'Tune back to HDMI{self.hdmi_test}')
        self.makeInstructionLabel("Launch and Playback YouTube")
        self.makeInstructionLabel(f'Tune back to HDMI{self.hdmi_test}')

    def runThis(self):
        """
        Below is where you assemble test cases
        """

        # Tune to HDMI currently testing
        self.launch_hdmi_input(f'HDMI{self.hdmi_test}')

        # Press RC POWER Key 3 times
        for i in range(0, 3):
            print(f'RC OFF cycle: {i}')
            self.press_rc_key("POWER")
            self.wait_second(5)
            self.press_rc_key("POWER")
            self.wait_second(3)

        # Let TV stabalize
        self.wait_second(5)

        # Input Change 3 times
        for i in range(0, 3):
            self.launch_hdmi_input(f'HDMI{self.hdmi_test}')
            self.wait_second(5)
            self.launch_hdmi_input("HDMI1")
            self.wait_second(5)

            self.launch_hdmi_input(f'HDMI{self.hdmi_test}')
            self.wait_second(5)
            self.launch_hdmi_input("HDMI2")
            self.wait_second(5)

            self.launch_hdmi_input(f'HDMI{self.hdmi_test}')
            self.wait_second(5)
            self.launch_hdmi_input("HDMI3")
            self.wait_second(5)

            self.launch_hdmi_input(f'HDMI{self.hdmi_test}')
            self.wait_second(5)
            self.launch_hdmi_input("HDMI4")
            self.wait_second(5)

            self.launch_hdmi_input(f'HDMI{self.hdmi_test}')
            self.wait_second(5)
            self.launch_tv_input()
            self.wait_second(5)

        # Tune to HDMI currently testing
        self.launch_hdmi_input(f'HDMI{self.hdmi_test}')
        self.wait_second(5)

        # Do trickplay
        if self.device_type == '1':
            # Do Channel Up every 10 minutes for 1 hour
            for i in range(1, 4):
                print(f'loop count {i}')
                self.channel_up()
                self.wait_second(10)
            # Do Channel Down every 10 minutes for 1 hour
            for i in range(1, 4):
                print(f'loop count {i}')
                self.channel_down()
                self.wait_second(10)
            # Trickplay
            self.press_rw(3)
            self.press_play()
            self.press_ff(3)
            self.press_play()
        else:
            # Trickplay Media box
            for i in range(0, 3):
                self.press_ff(3)
                self.press_play()
                self.press_rw(3)
                self.press_play()


# Select HDMI to test
device = input("Device Type: (Enter 1 for STB, 2 for Media Boxes): ")
start = input("Enter which HDMI you want to test (1, 2, 3 or 4): ")

# Start the script
root = Tk()
TestScript(root, start, device).startApp()
