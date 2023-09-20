userinput = ""

def difficultyselect(userinput):
    userinput = input("Please choose a difficulty level, easy or hard: ")
    if userinput == "easy" or "hard":
     return userinput

difficultyselect(userinput)
print(userinput)