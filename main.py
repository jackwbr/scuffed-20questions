objects = ['potato', 'test', 'object']
print(f"Here are your options, please choose one: {', '.join(objects)}")

index = 0

input("Please choose an option: ")

def falseinput():
    input("Please choose a valid option: ")

if input not in objects:   
    falseinput() 

def brute():
    while True:
        input(f"Is your object {objects[0]}? Please respond with yes or no: ")
        if input == "yes":
            print("I knew it!") 
            break

        elif input == "no":
            index += 1
            input(f"Is your object {objects[index]}? Please respond with yes or no: ")