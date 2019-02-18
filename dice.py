import random
import sys

def playAgain():
    play = input("Would you like to play again? \"y\" or \"n\": ")
    
    if play == "y" or play == "Y":
        dice()
    else:
        sys.exit()

def printRoll(r1, r2):
    print("")
    print("----- -----")
    print("| " + str(r1) + " | | " + str(r2) + " |")
    print("----- -----")
    print("Your current roll is " + str(r1 + r2) + ".")
    
def checkRoll(roll, point):
    if roll == 7 or roll == 11:
        print("")
        print("You hit " + str(roll) + ". You lose.")
        playAgain()
    
    elif roll == 2:
        print("")
        print("You hit snake eyes. You lose.")
        playAgain()
        
    elif roll == point:
        print("")
        print("You hit your point, " + str(point) +  ". You win.")
        playAgain()

def dice():
    die = [1,2,3,4,5,6]
    firstRoll1 = random.choice(die)
    firstRoll2 = random.choice(die)
    point = firstRoll1 + firstRoll2
    
    printRoll(firstRoll1, firstRoll2)
    
    if point == 7 or point == 11:
        print("")
        print("You hit " + str(point) + ". You win.")
        playAgain()
        
    elif point == 2:
        print("")
        print("You hit snake eyes. You lose.")
        playAgain()
        
    else:
        print("Your point is " + str(point) + ".")
        user = input("Roll again? \"y\" or \"n\": ")
        
        if user == "y" or user == "Y":
            pass
        else:
            sys.exit()
        
        currRoll = 0
        
        while currRoll != point and currRoll != 1 and currRoll != 7 and currRoll != 11:
            currRoll1 = random.choice(die)
            currRoll2 = random.choice(die)
            currRoll = currRoll1 + currRoll2
            
            printRoll(currRoll1, currRoll2)
            checkRoll(currRoll, point)
            
            print("")
            user = input("Roll again? \"y\" or \"n\": ")
            if user == "y" or user == "Y":
                continue
            else:
                sys.exit()
        
dice()