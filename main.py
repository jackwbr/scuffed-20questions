def difficultyselect():
    while True:
        userinput = input("Please select a difficulty, easy or hard: ")
        if userinput in ("easy", "hard"):
            print("good")
            break
        else:
            print("Please enter a valid difficulty")
            continue

difficultyselect()