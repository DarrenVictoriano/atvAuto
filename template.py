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
        super().__init__(tkRoot, "Template")  # Update the string

    def testCaseInfo(self):
        """ 
        Set the test case info
        This is the one that shows on the left side of the screen
        """
        self.makeInstructionLabel("Press Power Key")

    def runThis(self):
        """ Below is where you assemble test cases"""

        # Press RC POWER Key
        self.press_rc_key("POWER")
        self.wait_second(3)



# Start the script
root = Tk()
Demo(root).startApp()
