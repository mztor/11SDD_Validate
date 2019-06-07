from appJar import gui
import validate
app = gui()
app.addLabel("title", "ENTER DETAILS")
app.addLabelEntry("First Name")
app.addLabelEntry("Last Name")
app.addLabelEntry("Email")
app.addLabel("email", "")
app.addLabelEntry("Postcode")
app.addLabel("post", "")
app.addLabelEntry("Phone Number")
app.addLabelEntry("State")
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        fst = app.getEntry("First Name")
        scnd = app.getEntry("Last Name")
        eml = app.getEntry("Email")
        postcode = app.getEntry("Postcode")
        nmbr = app.getEntry("Phone Number")
        stt = app.getEntry("State")
        output = validate.validateEmail(eml)
        result = validate.validatePostcode(postcode)
    if output == 1:
        app.setLabel("email", "Your email is invalid")
    elif output == 0:
        app.clearLabel("email")
    if result == 1:
        app.setLabel("post", "Your postcode is invalid")
    else:
        app.clearLabel("post")

app.addButtons(["Submit", "Cancel"], press)
app.setBg("MediumAquamarine")
app.go()
