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

#katelyn and paris; purpose mobile number
def ValidateNumber():
    phoneNumber = input("Enter your phone number  ")
    if phoneNumber[0:2]  == "04" and len(phoneNumber) == 20:
        print("Phone number is valid")
    else:
        print("Phone number is invalid")


def ValidatePostcode():
    if postcode.len() != 4:
        print("Your postcode is invalid!")
        return 1
    else:
        print("Your postcode is valid!")
        return 0

def ValidatePassword():
   

def ValidateState():


