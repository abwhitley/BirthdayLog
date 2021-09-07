# Austin Whitley
# Assignment 4

# Birthday Dictionary

# Used as global to it can be used program wide
birthdayDictionary = {"Austin":"08/07/1994", "Nathan":"06/07/1994", "Blake":"06/18/1962","Brandy":"03/04/2964"}

def main():
    functionDictionary = {"Look Up a Birthday": lookUpBirthday, "Add a New Birthday": addBirthday, "Change a Birthday":changeBirthday, "Delete a Birthday": deleteBirthday}
    displayBirthdays()
    programRunning = True
    displayFunctions(functionDictionary)
    # while programRunning = True:

    print("\nWelcome to the Birthday Log\n")



def addBirthday():
    name = input("Enter a name: ")
    birthday = input("Enter a birthday: ")
    birthdayDictionary[name.title()] = birthday
    displayBirthdays()

def displayBirthdays():
    print("\nBIRTHDAYS")
    for name, birthday in birthdayDictionary.items():
        print("-------------------------")
        print(f"{name}: {birthday}")
        print("-------------------------")
    print("\n")

def deleteBirthday():
    names = []
    for name in birthdayDictionary.keys():
        names.append(name)
    print(names)
    nameToDelete = input("Enter the name you would like to remove: ")
    if nameToDelete.title in names:
        del birthdayDictionary[name]
        displayBirthdays()
    else:
        print("Please enter a valid name")
        deleteBirthday()

def changeBirthday():
    names = []
    for name in birthdayDictionary.keys():
        names.append(name)
    print(names)
    nameToChange = input("Which name would you like change the birthday: ").title()
    if nameToChange in names:
        birthday = input("Enter new birthday: ")
        birthdayDictionary[name] = birthday
        displayBirthdays()
    else:
        print("Please enter a valid name")
        changeBirthday()

def lookUpBirthday():
    names = []
    for name in birthdayDictionary.keys():
        names.append(name)
    birthdayToLookUp = input("Enter a name you would like to see the birtday for: ").title()
    if birthdayToLookUp in names:
        birthday = birthdayDictionary[birthdayToLookUp]
        print(f"{birthdayToLookUp}'s birthday is {birthday}'")
    else:
        print("Please enter a valid name")
        lookUpBirthday()

def displayFunctions(functionDictionary):
    count = 1
    print("\nOptions:")
    for functionName in functionDictionary.keys():
        print(f"{count}: {functionName}")
        count = count + 1
 


main()