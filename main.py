def difficulty():
    difficultylevel = input("Please choose a difficulty level, easy or hard:")
    while True:
        if difficultylevel == "easy" or "hard":
            break  
        else:
            print("Please choose a valid difficulty level")
            continue
difficulty()

indexalpha = 0
theobjects = ['potato', 'test', 'yesandno']
print("These are your options") 
print(*theobjects)                                       #ADD DIFICULTY LEVELS   

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

if difficulty == "easy":
    userinput()
    
scuffed(indexalpha)