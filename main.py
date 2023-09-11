indexalpha = 0
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

def scuffed(indexalpha):
    while True:
        input5 = input(f"Is what you are thinking of {theobjects[indexalpha]}? Please respond with yes or no:")
        if input5 == "yes":
            break

        else:
            indexalpha += 1
            continue


userinput()
scuffed(indexalpha)