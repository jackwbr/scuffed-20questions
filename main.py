def difficulty():
    difficultylvl = input("Please choose a difficulty level, easy or hard: ")  #EASY MEANS THE COMPUTER GUESSES IT IMMEDIATLY
    while True:
        if difficultylvl == "easy" or "hard":
            return difficultylvl
            break  
        else:
            print("Please choose a valid difficulty level")
            continue


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

#END THE DEFINING OF FUNCTIONS

difficulty() 

indexalpha = 0
theobjects = ['potato', 'test', 'yesandno']
print("These are your options, please think of one") 
print(*theobjects)                                       #ADD DIFICULTY LEVELS   

difficultylvl = difficulty()

if difficultylvl == "easy":
    userinput1 = userinput()
    print(f"Is what you are thinking of {userinput1}?")

if difficultylvl == "hard":
    scuffed(indexalpha)