import json
attributesIndex = 0

def createAcct():
    userAttributes = ("first name: ","last name: ","email: ")
    global attributesIndex
    
    #makes input be a certain format
    def validateInput(x):
        global attributesIndex
        error = True
        while(error == True):
            if(len(x) == 0):
                print("\n>>error: must enter value\n")
                x = input(userAttributes[attributesIndex])
            #makes sure email has '@' symbol
            elif(attributesIndex == 2):
                correctEmailFormat = False
                for i in x:
                    if(i == "@"):
                        correctEmailFormat = True
                        break
                    else:
                        continue
                if(correctEmailFormat == False):
                    print("\n>>error: invalid email format\n")
                    x = input(userAttributes[attributesIndex])
                else:
                    error = False
                    attributesIndex += 1
                    return x
            else:
                error = False
                attributesIndex += 1
                return x
                    
    fname = input("first name: ")
    fname = validateInput(fname)
    fname = fname.lower()
    lname = input("last name: ")
    lname = validateInput(lname)
    lname = lname.lower()
    email = input("email: ")
    email = validateInput(email)
    email = email.lower()

    # assigns user input into python obj
    userProfile = {
        "fname": fname,
        "lname": lname,
        "email": email
    }

    # gets json from data.json
    with open("/users/alex/documents/python/json-login-master/data.json", "r") as x:
        jsonStr = x.read() # returns raw json string
        pythonObj = json.loads(jsonStr) #converts json string into python dict
        pythonObj["users"].append(userProfile)
    # appends new json data to data.json
    with open("/users/alex/documents/python/json-login-master/data.json", "w") as y:
        x = json.dumps(pythonObj, indent=4)
        appendData = y.write(x)

    attributesIndex = 0

    print("\naccount created!\n")

def editAcct():
    # gets json from data.json
    with open("/users/alex/documents/python/json-login-master/data.json", "r") as x:
        jsonStr = x.read() # returns raw json string
        pythonObj = json.loads(jsonStr) #converts json string into python dict    
    #searches for matching email strings 
    def lookupEmail(x):
        foundEmail = False
        for i in pythonObj["users"]:
            if(i["email"] == x):
                foundEmail = True
                print("first name - " + i["fname"] + "\nlast name - " + i["lname"])
                newFname = input("new first name: ")
                newFname = newFname.lower()
                i["fname"] = newFname
                newLname = input("new last name: ")
                newLname = newLname.lower()
                i["lname"] = newLname
                # appends new json data to data.json
                with open("/users/alex/documents/python/json-login-master/data.json", "w") as y:
                    x = json.dumps(pythonObj, indent=4)
                    appendData = y.write(x)
                print("\naccount succesully changed!\n")     
                break
            else:
                continue

        if(foundEmail == False):
            print("\nemail not found\n")

    userEmail = input("enter email associated with account: ")
    lookupEmail(userEmail)