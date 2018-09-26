# First import the ADB_Action_Script.py it must be on the same folder
from daaf.ADB_Action_Scipt import ActionScript
# then import the RC keys and App PKGs for easy scripting
from daaf.RC_Code import SonyRCKey
from daaf.AppList import AppList

# create an instance of the class, variables can be change
tv = ActionScript()
rc = SonyRCKey()
app = AppList()
"""
# Format UI
ui.setIcon("img/bot_icon.ico")
ui.setBg("#B0D1CE")
ui.setSticky("NEW")
ui.setStretch("COLUMN")
counter = 10


def countdown():
    if counter > 0:
        ui.setLabel("count", str(counter))
        counter -= 1
        ui.after(1000)


def f2():
    ui.addLabel("2", "Do testcase 2", row=1, column=0)
    ui.addLabel("count", row=0, column=1)
    ui.setLabelBg("2", "#ccc")


def f3():
    ui.addLabel("2", "Do testcase 2", row=3, column=0)
    ui.setLabelBg("2", "#ccc")


# Automation Start
# ------------------------------- HDMI1 ----------------------------------
ui.addLabel("1", "Do testcase 1", row=0, column=0)
ui.addLabel("count", row=0, column=1)
ui.setLabelBg("1", "#fff")

ui.after(21000, f2)


# ------------------------ Launch GUI -----------------------------
ui.registerEvent(countdown)
ui.go()
"""
