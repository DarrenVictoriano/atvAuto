# import the library
from appJar import gui


def samplTest():
    ui.addLabel("1", "Welcome to appJar1")
    ui.setLabelBg("1", "#ccc")


def samplTest2():
    ui.addLabel("2", "Welcome to appJar2")
    ui.setLabelBg("2", "#fff")


def samplTest3():
    ui.addLabel("3", "Welcome to appJar1")
    ui.setLabelBg("3", "#ccc")


def samplTest4():
    ui.addLabel("4", "Welcome to appJar2")
    ui.setLabelBg("4", "#fff")


# create a GUI variable called app
ui = gui("Test", "768x480")
ui.setIcon("img/bot_icon.ico")
ui.setBg("#B0D1CE")

ui.startFrame("1", row=0, column=0)
ui.setSticky("NEW")
ui.setStretch("COLUMN")

# add & configure widgets - widgets get a name, to help referencing them later
ui.after(1000, samplTest)
ui.after(2000, samplTest2)
ui.after(3000, samplTest3)
ui.after(4000, samplTest4)
ui.stopFrame()


# start the GUI
ui.go()
