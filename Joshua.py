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
        print("First Name:", fst)
        print("Last Name:", scnd)
        print("Email:", eml)
        print("Postcode:", pst)
        print("Phone Number:", nmbr)
        print("State:", stt)
        output = validate.validateEmail(eml)
    if output == 1:
        app.addLabel("invalid", "Your email is invalid")
    elif output == 0:
        app.clearLabel("invalid")
app.addButtons(["Submit", "Cancel"], press)
app.setBg("red")
app.go()
