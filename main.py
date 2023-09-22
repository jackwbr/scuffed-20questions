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
        global easydoinput
        options = ["potato", "test", "cheese", "spam", "eggs"]
        print(*options)
        while True:
            easydoinput = input("Please enter an option from the list above: ")
            if userinput in options:
                break
            else:     
                print("Please enter a valid option")
                continue        

def easydo():
    print(easydoinput)


#END OF FUNCTION DEFINITIONS

difficultyselect()
if userinput == "easy":
    easy()


if userinput == "hard":
    print("hard chosen test")