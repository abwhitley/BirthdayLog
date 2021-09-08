# Austin Whitley
# Assignment 4

# Birthday Dictionary

# Used as global to it can be used program wide
birthdayDictionary = {"Austin":"08/07/1994", "Nathan":"06/07/1994", "Blake":"06/18/1962","Brandy":"03/04/2964"}

# TODO make a function to choose option
# TODO create a conditional flow to continue the program as long as the user wants to
# TODO make a quit option
def main():
    functionDictionary = {"Look Up a Birthday": lookUpBirthday, "Add a New Birthday": addBirthday, "Change a Birthday":changeBirthday, "Delete a Birthday": deleteBirthday}
    displayBirthdays()
    programRunning = True
    print("\nWelcome to the Birthday Log\n")

    displayFunctions(functionDictionary)
    chooseOption(functionDictionary)
    # while programRunning = True:



# Function to add birthday
def addBirthday():
    name = input("Enter a name: ")
    birthday = input("Enter a birthday: ")
    birthdayDictionary[name.title()] = birthday
    displayBirthdays()

# Function to display birthday for testing
def displayBirthdays():
    print("\nBIRTHDAYS")
    for name, birthday in birthdayDictionary.items():
        print("-------------------------")
        print(f"{name}: {birthday}")
        print("-------------------------")
    print("\n")

# Function used to delete birthday
def deleteBirthday():
    # for loop to make a list of names to display for choosing
    names = []
    for name in birthdayDictionary.keys():
        names.append(name)
    print(names)
    # Takes user input then checks to see if name is in list
    nameToDelete = input("Enter the name you would like to remove: ")
    if nameToDelete.title in names:
        # If its in the list it deletes the dictionary entry
        del birthdayDictionary[name]
        displayBirthdays()
    else:
        # Else it recalls function until a name inputed correctly
        print("Please enter a valid name")
        deleteBirthday()

# Function used to change a birthday
def changeBirthday():
    names = []
    #  For loop used to display a name for users to choose from
    for name in birthdayDictionary.keys():
        names.append(name)
    print(names)
    # Takes user input to choose the name that the borthday should be changed
    nameToChange = input("Which name would you like change the birthday: ").title()
    # If the name inputed is in the list it will change the birthday for the given name in the dicitonary
    if nameToChange in names:
        birthday = input("Enter new birthday: ")
        birthdayDictionary[name] = birthday
        displayBirthdays()
    # Else it will ask the user to try again and the function is recalled
    else:
        print("Please enter a valid name")
        changeBirthday()

#  Function to look up the birthday for a name
def lookUpBirthday():
    # For loop used for displaying names for users to choose from
    names = []
    for name in birthdayDictionary.keys():
        names.append(name)
    # User is asked to input name they would like to see birthday of
    birthdayToLookUp = input("Enter a name you would like to see the birtday for: ").title()
    # If name is in list it shows the birthday for the names
    if birthdayToLookUp in names:
        birthday = birthdayDictionary[birthdayToLookUp]
        print(f"{birthdayToLookUp}'s birthday is {birthday}'")
    # Else the user will be asked to try again andthe function is recalled
    else:
        print("Please enter a valid name")
        lookUpBirthday()

# Function is used to display the main options for the program
# functionsDictionary is a dictionary that keys are the discription of the option and the value 
# is the actual function
def displayFunctions(functionDictionary):
    count = 1
    print("\nOptions:")
    for functionName in functionDictionary.keys():
        print(f"{count}: {functionName}")
        count = count + 1
 

# functionDictionary = {"Look Up a Birthday": lookUpBirthday, "Add a New Birthday": addBirthday, "Change a Birthday":changeBirthday, "Delete a Birthday": deleteBirthday}
def chooseOption(functionDictionary):
    functionList = []
    optionChosen = input("Enter the number for the option you choose (q to quit):")
    for function in functionDictionary.values():
        functionList.append(function)
    if int(optionChosen) == 1:
        functionList[int(optionChosen)-1]()
        displayFunctions()
        chooseOption()
    elif int(optionChosen) == 2:
        functionList[int(optionChosen) -1]()
        displayFunctions()
        chooseOption()
    elif int(optionChosen) == 3:
        functionList[int(optionChosen) -1]()
        displayFunctions()
        chooseOption()
    elif int(optionChosen) == 4:
        functionList[int(optionChosen) -1]()
        displayFunctions()
        chooseOption()
    elif optionChosen.lower() == "q":
        print("Goodbye")
    else:
        print("You entered an incorrect option. Please try again")
        chooseOption()  

main()