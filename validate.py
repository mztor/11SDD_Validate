import re

#JOSHUA DRAYTON
#MAKES SURE THAT EMAIL IS VALID, WITH ONE @ SYMBOL, AT LEAST ONE ., AND THE @ BEFORE THE ..
def validateEmail():
    email = input("Enter Email: ")
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


def validateNumber():
#Jayden Taylor
#Makes sure the postcode is four numbers, as per Australian standards
def validatePostcode():
    postcode = input("What is your postcode? ")
    if len(postcode) != 4:
        print("Your postcode is invalid!")
        return 1
    else:
        print("Your postcode is valid!")
        return 0

#Anthony and Caleb
#Tests if the input has at least one capital, number and special character
def validatePassword():
    a = "Password is invalid"
    password = input("Password: ")
    characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    numbers = re.compile('[1234567890]')
    if password.islower() == False:
        if (characters.search(password)) != None:
            if (numbers.search(password)) != None:
                print("Password is valid")
            else:
                print(a)
        else:
            print(a)
    else:
        print(a)


def validateState():
