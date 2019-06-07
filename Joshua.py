from appJar import gui
import validate
app = gui()
app.addLabel("title", "ENTER DETAILS")
app.addLabelEntry("First Name")
app.addLabelEntry("Last Name")
app.addLabelEntry("Email")
app.addLabelEntry("Postcode")
app.addLabelEntry("Phone Number")
app.addLabelEntry("State")
app.addLabel("invalid", "")
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        fst = app.getEntry("First Name")
        scnd = app.getEntry("Last Name")
        eml = app.getEntry("Email")
        pst = app.getEntry("Postcode")
        nmbr = app.getEntry("Phone Number")
        stt = app.getEntry("State")
        output = validate.validateEmail(eml)
        result = validate.validatePostcode()
    if output == 1:
        app.setLabel("invalid", "Your email is invalid")
    elif output == 0:
        app.clearLabel("invalid")

app.addButtons(["Submit", "Cancel"], press)
app.setBg("red")
app.go()
