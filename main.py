objects = ["potato", "test", "object"]
print(f"Here are your options, please choose one: {', '.join(objects)}")
indexalpha = 0

def userinput():
    while True:
        input0 = input("Please choose an option: ")     
        if input0 in objects:          #if the users input is valid e.g. in the list, the loop breaks
            break
        else:                          #if the users input is not valid e.g. in the list, the loop conintues
            continue

userinput()                             # This calls the userinput function to get the users input



# def brute():
#     for x in range(20):
#         input(f"Is your object {objects[0]}? Please respond with yes or no: ")
#         if input == "yes":
#             print("I knew it!") 
#             break

#         elif input == "no":
#             index += 1
#             input(f"Is your object {objects[index]}? Please respond with yes or no: ")
