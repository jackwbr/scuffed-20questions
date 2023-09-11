theobjects = ['potato', 'test', 'yesandno']
print("These are your options") 
print(theobjects)

def userinput():
    while True:
        userinput1 = input("Please choose an option: ")
        if userinput1 in theobjects:
            break
        else:
            print("Please choose a valid option")

def scuffed():
    while True:

userinput()