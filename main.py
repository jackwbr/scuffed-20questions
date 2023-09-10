objects = ['potato', 'test', 'object']
print(f"Here are your options, please choose one: {', '.join(objects)}")

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

