# import the library
from appJar import gui
# create a GUI variable called app
app = gui("Test", "768x480")
app.setBg("#B0D1CE")

app.addLabel("counter")
app.setLabelBg("counter", "#fff")

counter = 10


def countdown():
    global counter
    if counter > 0:
        app.setLabel("counter", str(counter))
        counter -= 1
        app.after(1000)


app.registerEvent(countdown)

app.go()
