import json
attributesIndex = 0

def createAcct():
    userAttributes = ("first name: ","last name: ","email: ")
    global attributesIndex
    
    #makes email string have '@' symbol
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

    #makes input be a certain format
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

    # assigns user input into python obj
    userProfile = {
        "fname": fname,
        "lname": lname,
        "email": email
    }

    # gets json from data.json
    getJsonData = open("/users/alex/documents/python/json-login-master/data.json", "r")
    jsonStr = getJsonData.read() # returns raw json string
    pythonObj = json.loads(jsonStr) #converts json string into python dict
    pythonObj["users"].append(userProfile)
    # appends new json data to data.json
    appendJsonData = open("/users/alex/documents/python/json-login-master/data.json", "w")
    x = json.dumps(pythonObj, indent=4)
    appendData = appendJsonData.write(x)

    getJsonData.close()
    appendJsonData.close()
    attributesIndex = 0

    print("\naccount created!\n")

def editAcct():    
    #searches for matching email in 
    def lookupEmail(x):
        # gets json from data.json
        getJsonData = open("/users/alex/documents/python/json-login-master/data.json", "r")
        jsonStr = getJsonData.read() # returns raw json string
        pythonObj = json.loads(jsonStr) #converts json string into python dict
        getJsonData.close()
        # appends new json data to data.json
        appendJsonData = open("/users/alex/documents/python/json-login-master/data.json", "w")

        foundEmail = False
        for i in pythonObj["users"]:
            #if email exists
            if(i["email"] == x):
                foundEmail = True
                print("first name - " + i["fname"] + "\nlast name - " + i["lname"])
                newFname = input("new first name: ")
                i["fname"] = newFname
                newFname = input("new last name: ")
                i["lname"] = newFname
                x = json.dumps(pythonObj, indent=4)
                appendData = appendJsonData.write(x)
                appendJsonData.close()
                print("account succesully changed!")     
                break
            else:
                continue
        if(foundEmail == False):
            print("email not found")

    loop = True
    while(loop == True):
        userEmail = input("enter email associated with account: ")
        lookupEmail(userEmail)