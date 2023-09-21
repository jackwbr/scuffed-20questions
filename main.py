global userinput
def difficultyselect():
    global userinput
    while True:
        userinput = input("Please select a difficulty, easy or hard: ")
        if userinput in ("easy", "hard"):
            break
        else:
            print("Please enter a valid difficulty")
            continue

def easy():
    if userinput == "easy":
        options = ["potato", "test", "cheese", "spam", "eggs"]
        print(*options)
        while True:
            userinput = input("Please enter an option from the list above: ")
            if userinput in options:
                break
            else:     
                print("Please enter a valid option")
                continue        


#END OF FUNCTION DEFINITIONS

difficultyselect()
if userinput == "easy":
    easy()