# import the library
from appJar import gui
import validate

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        first = app.getEntry("First Name")
        last = app.getEntry("Last Name")
        mail = app.getEntry("Email")
        code = app.getEntry("Postcode")
        num = app.getEntry("Phone Number")
        state = app.getEntry("State")
        validate.validatePostcode(code)
# create a GUI variable called app
app = gui()

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "New User")
app.setBg("lightblue")
app.addLabelEntry("First Name")
app.addLabelEntry("Last Name")
app.addLabelEntry("Email")
app.addLabelEntry("Postcode")
app.addLabelEntry("Phone Number")
app.addLabelEntry("State")

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)
app.go()
