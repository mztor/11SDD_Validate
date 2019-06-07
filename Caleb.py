from appJar import gui
import validate

app = gui("Login Window", "400x200")
app.setBg("purple")
app.setFont(18)

app.addLabelEntry("First Name")
app.addLabelEntry("Last Name")
app.addLabelSecretEntry("Password")
app.addLabelEntry("Email")
app.addLabelEntry("Phone")

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        fName = app.getEntry("First Name")
        lName = app.getEntry("Last Name")
        password = app.getEntry("Password")
        email = app.getEntry("Email")
        phone = app.getEntry("Phone")

        print("First Name:", fName)
        print("Last Name:", lName)
        print("Password: ", password)
        print("Email:", email)
        print("Phone:", phone)

    validate.validatePassword(password)
    validate.validateEmail(email)
    validate.validateNumber(phone)

app.addButtons(["Cancel", "Submit"], press)

app.go()