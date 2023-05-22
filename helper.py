# ITP 115, Spring 2023
# Final Project
# Name: Vivek Raheja
# Email: vraheja@usc.edu
# Section: 31836
# Filename: helper.py
# Description: helper file that defines helper functions to be used in user_io.py and main.py

# Parameter: filenameStr is the name of the CSV file to read and set a default
# value of "roller_coasters.csv"
# Return value: a list of dictionaries where each dictionary represents one roller
# coaster. For each dictionary, the keys are the strings from the header row
# and the values are strings containing the information from one row of the
# CSV file.

def makeCoastersList(filenameStr = "roller_coasters.csv"):

    coastersList = []
    file = open(filenameStr, "r")
    keys = file.readline().strip().split(",") # retrieving keys
    for line in file:
        line = line.strip().split(",")
        coastersDict = {}
        for i in range(len(keys)):
            coastersDict[keys[i]] = line[i] # creating coastersDict by creating key, value pairs
        coastersList.append(coastersDict)

    file.close() # close
    return coastersList

# Parameter: coastersList is a list of dictionaries where each dictionary
# represents a roller coaster
# Return value: a list of strings where each string is the name of a park; this list
# will contain the names of unique parks (strings) in alphabetical order

def getUniqueParkNames(coasterList):

    parkNames = []
    for coaster in coasterList:
        parkName = coaster['park']
        while parkName not in parkNames: # ensures uniqueness
            parkNames.append(parkName) # adding to list

    parkNames.sort()
    return parkNames

# Parameter: coastersList is a list of dictionaries where each dictionary
# represents a roller coaster
# Return value: a dictionary containing one coaster, which has the largest value
# for num_inversions (i.e., number of loops

def getLoopiestCoaster(coasterList):
    loopyCoaster = {}
    largestNumberLoops = 0

    for coaster in coasterList:
        loopNumber = coaster['num_inversions'] # getting string value at key = 'num_inversions'
        if loopNumber.isdigit() is True: # checking if digit
            loopNumber = int(loopNumber)
            if loopNumber > largestNumberLoops:
                largestNumberLoops = int(loopNumber)
                loopyCoaster = coaster

    return loopyCoaster

# Parameter: coastersList is a list of dictionaries where each dictionary
# represents a roller coaster
# Return value: a dictionary containing one coaster, which has the largest value
# for height

def getTallestCoaster(coasterList):

    largestHeight = 0 # declaring largestHeight variable to 0
    tallestCoaster = {}

    for coaster in coasterList:
        height = coaster['height']
        if height.isdigit() is True:
            height = int(height)
            if height > largestHeight: # updates max
                largestHeight = height
                tallestCoaster = coaster

    return tallestCoaster
