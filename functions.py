import json

def createAcct():
    userAttributes = ("first name: ","last name: ","email: ")
    attributesIndex = 0

    def validateInput(x):
        error = True
        while(error == True):
            if(len(x) == 0):
                print("\n>>error: must enter value\n")
                x = input(userAttributes[attributesIndex])
            else:
                return x
                error = False
                    
    fname = input("first name: ")
    fname = validateInput(fname)
    lname = input("last name: ")
    lname = validateInput(lname)
    email = input("email: ")
    email = validateInput(email)


    # assigns user values into python dict
    userProfile = {
        "fname": fname,
        "lname": lname,
        "email": email
    }

    # gets json from data.json
    getJsonData = open("/users/alex/documents/data.json", "r")
    jsonStr = getJsonData.read() # returns raw json string
    pythonObj = json.loads(jsonStr) #converts json string into python dict
    pythonObj["users"].append(userProfile)
    # appends new json data to data.json
    appendJsonData = open("/users/alex/documents/data.json", "w")
    x = json.dumps(pythonObj, indent=4)
    appendData = appendJsonData.write(x)

    getJsonData.close()
    appendJsonData.close()

    print("\naccount created!\n")








