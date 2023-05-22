# ITP 115, Spring 2023
# Final Project
# Name: first last
# Email: vraheja@usc.edu
# Section: 31836
# Filename: user_io.py (update accordingly)
# Description: this file defines all functions for the user interface,
# anything that the user inputs or is displayed to the user has a function in this file

import helper


# Parameter: optionsDict is a dictionary with the options and their descriptions
# Return value: None
def displayDict(optionsDict):
    keyList = optionsDict.keys() # getting keys from options dictionary
    keyList = list(keyList)
    keyList.sort()
    for key in keyList:
        print(key + " -> " + optionsDict[key])

# Parameter: optionsDict is a dictionary with the user’s options
# Return value: a string that is a valid option entered by the user
def getUserOption(optionsDict):
    option = input("Option: ")
    option = option.upper().strip()

    while option not in optionsDict: # loop until user enters an input in options dictionary
        option = input("Option: ")
        option = option.upper().strip()

    return option

# Parameter: coastersList is a list of dictionaries where each dictionary
# represents a roller coaster
# Return value: None
def displayNumCoasters(coastersList):
    print("The total number of coasters is " + str(len(coastersList)))


# Parameter: coastersList is a list of dictionaries where each dictionary
# represents a roller coaster
# Return value: None
def displayNumWoodenCoasters(coastersList):
    numWoodenCoasters = 0
    for coaster in coastersList:
        if coaster['material_type'] == "Wooden": # retrieving coasters where value of key is "Wooden"
            numWoodenCoasters += 1

    print("The total number of wooden coasters is " + str(numWoodenCoasters))

# Parameter: coasterDict is a dictionary holding the data for one coaster
# Return value: None
def displayCoaster(coasterDict):
    name = coasterDict['name']  # getting values based on respective key
    park = coasterDict['park']
    speed = coasterDict['speed']
    height = coasterDict['height']
    length = coasterDict['length']
    status = coasterDict['status']
    loops = coasterDict['num_inversions']

    # printing park and characteristics
    print(name + " " + "[" + park + "]")

    if speed != "":
        print("     Speed = " + speed + " mph")

    if height != "":
        print("     Height = " + height + " ft")

    if length != "":
        print("     Length = " + length + " ft")

    if loops != "" and int(loops) > 0:
        print("     Loops = " + loops)

    print("     Status is " + status)


# Parameter: coastersList is a list of dictionaries where each dictionary
# represents a roller coaster
# Return value: None
def displayLoopiestCoaster(coastersList):
    loopiestCoaster = helper.getLoopiestCoaster(coastersList) # function defined in helper.py, retrieves loopiest coaster in coasterList
    displayCoaster(loopiestCoaster)

# Parameter: coastersList is a list of dictionaries where each dictionary
# represents a roller coaster
# Return value: None
def displayTallestCoaster(coastersList):
    tallestCoaster = helper.getTallestCoaster(coastersList)
    displayCoaster(tallestCoaster)

# Parameter: coastersList is a list of dictionaries where each dictionary
# represents a roller coaster
# Return value: None
def makeParksFile(coastersList):
    uniqueParks = helper.getUniqueParkNames(coastersList) # defined in helper.py, gets names from dictionary coasterList
    uniqueParks.sort()
    numParks = len(uniqueParks)

    filename = "amusement_parks.txt"
    f = open(filename, "w")

    f.write("Amusement parks in alphabetical order:")
    f.write("\n")

    for park in uniqueParks:

        f.write(park + "\n")

    print("There are " + str(numParks) + " unique parks.")
    print("The park names were saved to amusement_parks.txt")


# Parameter: coastersList is a list of dictionaries where each dictionary
# represents a roller coaster
# Return value: None
def findCoasters(coastersList):
    counter = 0
    search = input("Enter a search phrase: ").strip().lower()

    for coaster in coastersList:
        coasterName = coaster['name'].lower() # getting value at key = 'name'
        parkName = coaster['park'].lower()
        if search in coasterName or search in parkName: # search can be present in the coaster's name or the park's name.
                counter += 1
                displayCoaster(coaster)

    if counter > 0:
        print("Found " + str(counter) + " coasters that contain " + "\'" + search + "\'")
    else:
        print("No coasters contain", "\'" + search + "\'")




