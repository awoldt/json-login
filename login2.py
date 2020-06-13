import functions

loop = True
while(loop == True):
    userCommand = input("create, edit or delete account: ")
    if userCommand == "create":
        userData = functions.createAcct() #fname, lname, and email info returned
    else:
        print("error")

