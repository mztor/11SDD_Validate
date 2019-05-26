#JOSHUA DRAYTON
#MAKES SURE THAT EMAIL IS VALID, WITH ONE @ SYMBOL, AT LEAST ONE ., AND THE @ BEFORE THE ..
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
    if postcode.len() != 4:
        print("Your postcode is invalid!")
        return 1
    else:
        print("Your postcode is valid!")
        return 0

def ValidatePassword():


def ValidateState():




ValidateEmail()