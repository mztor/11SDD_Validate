from appJar import gui
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
    validateEmail(eml)
def validateEmail(eml):
    email = eml
    amount = int(email.count("@"))
    if amount == 1:
        if "." in email:
            pos1 = int(email.find("@"))
            pos2 = int(email.find("."))
            if pos1 < pos2:
                print("Your email is valid!")
            else:
                print("Your email is invalid!")
        else:
            print("Your email is invalid!")
    else:
        print("Your email is invalid!")
app.addButtons(["Submit", "Cancel"], press)
app.setBg("red")
app.go()
