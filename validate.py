
import re


#JOSHUA DRAYTON
#MAKES SURE THAT EMAIL IS VALID, WITH ONE @ SYMBOL, AT LEAST ONE ., AND THE @ BEFORE THE ..
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

#katelyn and paris; purpose mobile number
def validateNumber():

    phoneNumber = input("Enter your phone number  ")
    if phoneNumber[0:2]  == "04" and len(phoneNumber) == 20:
        print("Phone number is valid")
    else:
        print("Phone number is invalid")


    




#Jayden Taylor
#Makes sure the postcode is four numbers, as per Australian standards
def validatePostcode(postcode):
    if len(postcode) != 4:
        print("Your postcode is invalid!")
        return 1
    else:
        print("Your postcode is valid!")
        return 0



def ValidateState():
    State = input("What state do you live in? ")
    if State == "NSW":
        print("This is a valid state")
    elif State == "VIC":
        print("This is a valid state")
    elif State == "NT":
        print("This is a valid state")
    elif State == "QLD":
        print("This is a valid state")
    elif State == "SA":
        print("This is a valid state")
    elif State == "WA":
        print("This is a valid state")
    elif State == "TAS":
        print("This is a valid state")
    else:
        print("This ias an invalid state")

#Anthony and Caleb
#Tests if the input has at least one capital, number and special character
def validatePassword(password):
    characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    numbers = re.compile('[1234567890]')
    if password.islower() == False:
        if (characters.search(password)) != None:
            if (numbers.search(password)) != None:
                print("Password is valid")
            else:
                print("Requires a special character")
        else:
            print("Requires a number")
    else:
        print("Requires an capital letter")


#def validateState():
#validateEmail()
#validatePassword()
#validatePostcode()


