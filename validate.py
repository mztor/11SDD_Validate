import re

def ValidateEmail():
    Email = input("Enter Email: ")
    if "@" in email:
        print(hi)

def ValidateNumber():


def ValidatePostcode():


def ValidatePassword():
    #Anthony and Caleb
    password = input("Password: ")
    characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if password.islower() == False:
        if (characters.search(password)) != None:
            print("Password is valid")
        else:
            print("PROBLEM")
    else:
        print("Password is not Valid")


def ValidateState():

