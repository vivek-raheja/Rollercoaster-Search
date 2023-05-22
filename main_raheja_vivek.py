# ITP 115, Spring 2023
# Final Project
# Name: Vivek Raheja
# Email: vraheja@usc.edu
# Section: 31836
# Filename: main_raheja_vivek.py (update accordingly)
# Description: (you fill in)

import helper

import user_io

# Parameter: None
# Return value: a dictionary where the keys are letters for the user to input and
# the values are descriptions for each option.
def makeOptionsDict():
    # creating options dictionary for user to choose from
    optionsDict = {
        "A": "Amusement parks",
        "B": "Number of coasters",
        "C": "Number of wooden coasters",
        "D": "Loopiest coaster",
        "E": "Tallest coaster",
        "F": "Find coasters",
        "Q": "Quit"
    }
    return optionsDict


# Parameter: None
# Return value: None
def main():
    print("Roller Coasters from around the world")

    coastersList = helper.makeCoastersList()
    optionsDict = makeOptionsDict()

    user_io.displayDict(optionsDict)
    userChoice = user_io.getUserOption(optionsDict)

    while userChoice.lower() != "q":
        # choices mapped to their respective functions
        if userChoice == "A":
            user_io.makeParksFile(coastersList)
        elif userChoice == "B":
            user_io.displayNumCoasters(coastersList)
        elif userChoice == "C":
            user_io.displayNumWoodenCoasters(coastersList)
        elif userChoice == "D":
            user_io.displayLoopiestCoaster(coastersList)
        elif userChoice == "E":
            user_io.displayTallestCoaster(coastersList)
        elif userChoice == "F":
            user_io.findCoasters(coastersList)

        print(" ")
        user_io.displayDict(optionsDict)
        userChoice = user_io.getUserOption(optionsDict) # updates user choice before loop

main()