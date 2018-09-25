# First import the ADB_Action_Script.py it must be on the same folder
from daaf.ADB_Action_Scipt import ActionScript
# then import the RC keys and App PKGs for easy scripting
from daaf.RC_Code import SonyRCKey
from daaf.AppList import AppList
from appJar import gui

# create an instance of the class, variables can be change
tv = ActionScript()
rc = SonyRCKey()
app = AppList()
ui = gui("Sample2", "768x480")

# Format UI
ui.setIcon("img/bot_icon.ico")
ui.setBg("#B0D1CE")
ui.setSticky("NEW")
ui.setStretch("COLUMN")

loop_count = 5


def f1():
    ui.setLabel("1", "Launch Netflix")
    ui.setLabelBg("1",  "#fff")
    ui.setLabelFg("1", "#c10")
    print("Launch Netflix")


def f2():
    ui.setLabel("2", "Playback content")
    ui.setLabelBg("2",  "#ccc")
    ui.setLabelFg("1", "#000")
    ui.setLabelFg("2", "#c10")
    print("playback content")


def loop_em():
    global loop_count
    if loop_count > 0:
        ui.after(1000, f1)
        ui.after(10000, f2)
        print(f'loop count {loop_count}')
        clear_ui()
        loop_count -= 1


def clear_ui():
    global ui
    ui.removeAllWidgets()


# Automation Start
# ------------------------------- Labels ----------------------------------
ui.addEmptyLabel("1")
ui.addEmptyLabel("2")


# ------------------------ Launch GUI -----------------------------
ui.registerEvent(loop_em)
ui.go()
