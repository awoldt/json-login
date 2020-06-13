import json

def createAcct():
    fname = input("first name: ")
    lname = input("last name: ")
    age = input("age: ")

    # assigns user values to be stored in json file
    userProfile = {
        "fname": fname,
        "lname": lname,
        "age": age
    }

    # gets data from data.json
    getJsonData = open("/users/alex/documents/data.json", "r")
    jsonStr = getJsonData.read() # returns raw json string
    pythonObj = json.loads(jsonStr) #converts json string into python dict
    pythonObj["users"].append(userProfile)

    appendJsonData = open("/users/alex/documents/data.json", "w")
    x = json.dumps(pythonObj)
    appendData = appendJsonData.write(x)

    getJsonData.close()
    appendJsonData.close()








