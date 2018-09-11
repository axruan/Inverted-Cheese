# Alex Ruan
# September 11, 2018
# Inverted Robot Cheese
# Various threads on StackOverflow

from random import *

numCat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
numCheese = 0
numInvert = 0
print("Hello user, I am Inverted Cheese.")
username = input("What is your name?\n").capitalize()
print("Hello, " + username + "! Type 'help' to get started.")

while True:
    command = input()
    if command == "help":
        print("List of Commands:\nhello: Greets Inverted Cheese\ncat: Unboxes a cat\ninventory1: Shows the first part of the inventory\ninventory2: SHows the second part of the inventory\ncheese: Gives you a cheese\ninvert: Inverts your cheese\nnumcheese: Shows how much cheese you have\nstop: Ends the program.")
    elif command == "hello":
        print("Hello, " + username + "!")
    elif command == "cheese":
        print("Here is a cheese!")
        numCheese += 1
        print("You have " + str(numCheese) + " cheese")
    elif command == "invert":
        print("Inverting " + str(numCheese) + " cheese. . .")
        numInvert += numCheese
        print(str(numInvert) + " cheese inverted.")
    elif command == "numcheese":
        print("You have " + str(numCheese) + " cheese, " + str(numInvert) + " inverted cheese." )
    elif command == "cat":
        num = randint(0,11)
        if num == 0:
            numCat[num] += 1
            print("You now have " + str(numCat[num]) + " brown cats (common)")
        elif num == 1:
            numCat[num] += 1
            print("You now have " + str(numCat[num]) + " grey cats (common)")
        elif num == 2:
            numCat[num] += 1
            print("You now have " + str(numCat[num]) + " white cats (common)")
        elif num == 3:
            numCat[num] += 1
            print("You now have " + str(numCat[num]) + " black cats (common)")
        elif num == 4:
            numCat[num] += 1
            print("You now have " + str(numCat[num]) + " orange cats (common)")
        elif num == 5:
            numCat[num] += 1
            print("You now have " + str(numCat[num]) + " furless cats (rare)")
        elif num == 6:
            numCat[num] += 1
            print("You now have " + str(numCat[num]) + " hairy cats (rare)")
        elif num == 7:
            numCat[num] += 1
            print("You now have " + str(numCat[num]) + " fat cats (epic)")
        elif num == 8:
            numCat[num] += 1
            print("You now have " + str(numCat[num]) + " chubby cats (epic)")
        elif num == 9:
            numCat[num] += 1
            print("You now have " + str(numCat[num]) + " magic cats (legendary)")
    elif command == "inventory1":
        print("Inventory Part I:\n\nCommon Cats:\nBrown: " + str(numCat[0]) + "\nGrey " + str(numCat[1]) + "\nWhite: " + str(numCat[2]) + "\nBlack: " + str(numCat[3]) + "\nOrange: " + str(numCat[4]))
    elif command == "inventory2":
        print("Inventory Part II:\n\nRare Cats:\nFurless: " + str(numCat[5]) + "\nHairy: " + str(numCat[6]) + "\n\nEpic Cats:\nFat: " + str(numCat[7]) + "\nChubby: " + str(numCat[8]) + "\n\nLegendary:\nMagic: " + str(numCat[9]))
    elif command == "stop":
        break
