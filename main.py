userinput = ""

def difficultyselect(userinput):
    while True:
        userinput = input("Please choose a difficulty level, easy or hard: ")
        userinput = userinput.lower().strip()
        if userinput == "easy" or "hard":
         return userinput
        
        else: 
            print("Please choose a valid input: ")
            continue

difficultyselect(userinput)
print(userinput)