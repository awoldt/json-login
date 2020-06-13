import functions

loop = True
print("\n")
while(loop == True):
    userCommand = input("create, edit or delete account: ")
    userCommand = userCommand.lower()
    if(userCommand == "create"):
        userData = functions.createAcct() #fname, lname, and email info returned
    elif(userCommand == "edit"):
        print("edit!")
    elif(userCommand == "delete"):
        print("delete!")
    elif(userCommand == "exit"):
        exit()
    else:
        print("\n>>error: unknown command '" + userCommand + "'\n")
    
