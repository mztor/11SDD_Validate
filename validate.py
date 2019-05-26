def ValidateEmail():
    email = input("Enter Email: ")
    if "@" in email:
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


def ValidateNumber():


def ValidatePostcode():



def ValidatePassword():



def ValidateState():



