import json
attributesIndex = 0

def createAcct():
    userAttributes = ("first name: ","last name: ","email: ")
    global attributesIndex
    
    def isEmail(x):
        loop = True
        while(loop == True):
            for i in x:
                if(i == "@"):
                    loop == False
                    return x
                else:
                    continue
            print("\n>>error: invalid email")
            x = input("email: ")

    def validateInput(x):
        global attributesIndex
        error = True
        while(error == True):
            if(len(x) == 0):
                print("\n>>error: must enter value\n")
                x = input(userAttributes[attributesIndex])
            else:
                error = False
                attributesIndex += 1
                return x
                    
    fname = input("first name: ")
    fname = validateInput(fname)
    lname = input("last name: ")
    lname = validateInput(lname)
    email = input("email: ")
    email = validateInput(email)
    email = isEmail(email)

    # assigns user values into python dict
    userProfile = {
        "fname": fname,
        "lname": lname,
        "email": email
    }

    # gets json from data.json
    getJsonData = open("/users/alex/documents/json-login-master/data.json", "r")
    jsonStr = getJsonData.read() # returns raw json string
    pythonObj = json.loads(jsonStr) #converts json string into python dict
    pythonObj["users"].append(userProfile)
    # appends new json data to data.json
    appendJsonData = open("/users/alex/documents/json-login-master/data.json", "w")
    x = json.dumps(pythonObj, indent=4)
    appendData = appendJsonData.write(x)

    getJsonData.close()
    appendJsonData.close()
    attributesIndex = 0

    print("\naccount created!\n")

    








