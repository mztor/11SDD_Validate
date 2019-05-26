#JOSHUA DRAYTON
#MAKES SURE THAT EMAIL IS VALID, WITH ONE @ SYMBOL, AT LEAST ONE ., AND THE @ BEFORE THE ..
def ValidateEmail():
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


#def ValidateNumber():


#Jayden Taylor
#Makes sure the postcode is four numbers, as per Australian standards
def ValidatePostcode():
    postcode = input("What is your postcode? ")
    if len(postcode) != 4:
        print("Your postcode is invalid!")
        return 1
    else:
        print("Your postcode is valid!")
        return 0

#def ValidatePassword():


#def ValidateState():

ValidatePostcode()