# Austin Whitley
# Assignment 4

# Birthday Dictionary

# Used as global to it can be used program wide
birthdayDictionary = {"Austin":"08/07/1994", "Nathan":"06/07/1994", "Blake":"06/18/1962","Brandy":"03/04/2964"}

def main():
    functionDictionary = {"Look Up a Birthday": lookUpBirthday, "Add a New Birthday": addBirthday, "Change a Birthday":changeBirthday, "Delete a Birthday": deleteBirthday}
    print("\nWelcome to the Birthday Log\n")
    displayFunctions(functionDictionary)
    chooseOption(functionDictionary)

# Function controls the flow of the program and calls the other functions when the option is inputed
def chooseOption(functionDictionary):
    # functionDictionary = {"Look Up a Birthday": lookUpBirthday, "Add a New Birthday": addBirthday,
    # "Change a Birthday":changeBirthday, "Delete a Birthday": deleteBirthday}

    # Function used to display the options for the program
    functionList = []
    # Input used to choose option
    optionChosen = str(input("Enter the number for the option you choose ('q' to quit or 'd' to display dictionary):"))
    print("\n")
    
    # Loop used to take take the values of the functionDictionary and put into list
    # functionList is a list of functions that were stored in the dictionary
    for function in functionDictionary.values():
        functionList.append(function)
    # If else's used to take the user input and decide what function to use
    # I need to use the string anwsers first, when i tried to put them last i kept getting errors concering
    # how i convert the answers to ints for the other options
    if optionChosen.lower() == "q":
        print("Goodbye")
    # Added this option just to be able to display the birthday dictionary
    elif optionChosen.lower() == "d":
        displayBirthdays()
        displayFunctions(functionDictionary)
        chooseOption(functionDictionary)
    elif int(optionChosen) == 1:
        # This takes the option chossen and subtract 1 to find the correct index for the function list
        functionList[int(optionChosen)-1]()
        # Display the options for the program after the intial option chossen has run
        displayFunctions(functionDictionary)
        # Recall the function and this process continues until the 'q' is entered to quit
        chooseOption(functionDictionary)
    elif int(optionChosen) == 2:
        functionList[int(optionChosen) -1]()
        displayFunctions(functionDictionary)
        chooseOption(functionDictionary)
    elif int(optionChosen) == 3:
        functionList[int(optionChosen) -1]()
        displayFunctions(functionDictionary)
        chooseOption(functionDictionary)
    elif int(optionChosen) == 4:
        functionList[int(optionChosen) -1]()
        displayFunctions(functionDictionary)
        chooseOption(functionDictionary)
    else:
        print("You entered an incorrect option. Please try again")
        chooseOption(functionDictionary)  

# Function is used to display the main options for the program
# functionsDictionary is a dictionary that keys are the discription of the option and the value 
# is the actual function
def displayFunctions(functionDictionary):
    count = 1
    print("\nOptions:")
    for functionName in functionDictionary.keys():
        print(f"{count}: {functionName}")
        count = count + 1
    print("\n")

# Function to display birthday for testing
def displayBirthdays():
    print("\nBIRTHDAYS")
    for name, birthday in birthdayDictionary.items():
        print("-------------------------")
        print(f"{name}: {birthday}")
        print("-------------------------")
    print("\n")

# Function to add birthday
def addBirthday():
    name = input("Enter a name: ")
    birthday = input("Enter a birthday: ")
    birthdayDictionary[name.title()] = birthday

#  Function to look up the birthday for a name
def lookUpBirthday():
    # For loop used for displaying names for users to choose from
    names = []
    for name in birthdayDictionary.keys():
        names.append(name)
    print(f"Options:\n{names}\n")
    # User is asked to input name they would like to see birthday of
    birthdayToLookUp = input("Enter a name you would like to see the birtday for: ").title()
    # If name is in list it shows the birthday for the names
    if birthdayToLookUp in names:
        birthday = birthdayDictionary[birthdayToLookUp]
        print(f"\n{birthdayToLookUp}'s birthday is {birthday}\n")
    # Else the user will be asked to try again andthe function is recalled
    else:
        print("Please enter a valid name")
        lookUpBirthday()

# Function used to change a birthday
def changeBirthday():
    names = []
    #  For loop used to display a name for users to choose from
    for name in birthdayDictionary.keys():
        names.append(name)
    print(f"Options:\n{names}")
    # Takes user input to choose the name that the borthday should be changed
    nameToChange = input("Which name would you like change the birthday: ").title()
    # If the name inputed is in the list it will change the birthday for the given name in the dicitonary
    if nameToChange in names:
        birthday = input("Enter new birthday: ")
        birthdayDictionary[nameToChange] = birthday
    # Else it will ask the user to try again and the function is recalled
    else:
        print("Please enter a valid name")
        changeBirthday()

# Function used to delete birthday
def deleteBirthday():
    # for loop to make a list of names to display for choosing
    names = []
    for name in birthdayDictionary.keys():
        names.append(name)
    print(f"Options:\n{names}")
    # Takes user input then checks to see if name is in list
    nameToDelete = input("Enter the name you would like to remove: ")
    if nameToDelete.title() in names:
        # If its in the list it deletes the dictionary entry
        del birthdayDictionary[nameToDelete]
    else:
        # Else it recalls function until a name inputed correctly
        print("Please enter a valid name")
        deleteBirthday()

main()