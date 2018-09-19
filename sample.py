# import the library
from appJar import gui


# create a GUI variable called app
ui = gui("Test", "768x480")
ui.setBg("#B0D1CE")

# add & configure widgets - widgets get a name, to help referencing them later
ui.addLabel("title", "Welcome to appJar")
ui.setLabelBg("title", "#fff")


def samplTest():
    ui.addLabel("2", "Welcome to appJar")


ui.after(1000, samplTest)

# start the GUI
ui.go()
