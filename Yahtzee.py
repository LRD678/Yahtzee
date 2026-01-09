"""
	Description: Yahtzee
	Author: Landen Dwyer
	Date of first edit: Mon Jan  5 12:19:08 2026
"""

import random


players = []

validYNInputs = ["y", "n"]

curState = "Setup"

# HELPER FUNCTIONS

def validInput(question : str, validInputs : dict):
    validInp = False
    while validInp == False:
        inp = input(question)
        if inp in validInputs:
            return inp
        else:
            validInp = False
            print(f"{inp} is not a valid input please respond with {validInputs}")
      
# CORE GAME FUNCTIONS
        
def setupPlayers():
    
    # Get amount of players playing
    amountOfPlayers = int(input("How many players?\n"))
    while amountOfPlayers < 2:
        amountOfPlayers = int(input("Sorry you need at least 2 players, how many players?\n"))
        
    # Reset players dict incase you need to redo names
    global players
    players = []
    
    # Get all of the player names into the dictionary
    for player in range(0, amountOfPlayers):
        players.append(input(f"Insert player {player+1}'s name\n"))
        
    # Check if names are correct and finish game setup
    if validInput(f"The players are {players}, can I proceed? (y/n)\n", validYNInputs) == "y":
        players = random.shuffle(players)
        print("confirmed")
        global curState
        curState = "Playing"

# Setup the players
while curState == "Setup":
    setupPlayers()
    
    
# lines = ["======================== YAHTZEE SCORE SHEET ========================",
#          "                                                                     ",
#          "                          P1           P2           P3           P4  ",
#          "---------------------------------------------------------------------",
#          "UPPER SECTION                                                        ",
#          "Aces (1s)               | _ |        | _ |        | _ |        | _ | ",
#          "Twos (2s)               | _ |        | _ |        | _ |        | _ | ",    
#          "Threes (3s)             | _ |        | _ |        | _ |        | _ | ", 
#          "Fours (4s)              | _ |        | _ |        | _ |        | _ | ",
#          "Fives (5s)              | _ |        | _ |        | _ |        | _ | ",
#          "Sixes (6s)              | _ |        | _ |        | _ |        | _ | ",
#          "TOTAL                   | _ |        | _ |        | _ |        | _ | ",
#          "BONUS (35 if ≥63)       | _ |        | _ |        | _ |        | _ | ",
#          "UPPER TOTAL             | _ |        | _ |        | _ |        | _ | ",
#          "                                                                     ",
#          "LOWER SECTION                                                        ",
#          "3 of a Kind             | _ |        | _ |        | _ |        | _ | ",
#          "4 of a Kind             | _ |        | _ |        | _ |        | _ | ",
#          "Full House (25 pts)     | _ |        | _ |        | _ |        | _ | ",
#          "Small Straight (30 pts) | _ |        | _ |        | _ |        | _ | ",
#          "Large Straight (40 pts) | _ |        | _ |        | _ |        | _ | ",
#          "Yahtzee (50 pts)        | _ |        | _ |        | _ |        | _ | ",
#          "Chance                  | _ |        | _ |        | _ |        | _ | ",
#          "LOWER TOTAL             | _ |        | _ |        | _ |        | _ | ",
#          "Yahtzee Bonus (+100)    | _ |        | _ |        | _ |        | _ | ",
#          "                                                                     ",
#          "GRAND TOTAL             | _ |        | _ |        | _ |        | _ | ",
#          "====================================================================="
#          ]

# categories = {"Aces" : 6,
#              "Twos" : 7,
#              "Threes" : 8,
#              "Fours" : 9,
#              "Fives" : 10,
#              "Sixes" : 11,
#              "DiceTotalsUpper" : 12,
#              "DiceTotalBonus" : 13,
#              "UpperTotal" : 14,
#              "3OfAKind" : 17,
#              "4OfAKind" : 18,
#              "FullHouse" : 19,
#              "SmallStraight" : 20,
#              "LargeStraight" : 21,
#              "Yahtzee" : 22,
#              "Chance" : 23,
#              "LowerTotal" : 24,
#              "YahtzeeBonus" : 25,
#              "GrandTotal" : 17
#              }

# playerColumnIdx = {
#     1 : 27,
#     2 : 50,
#     3 : 63,
#     4 : 76
#     }

playerScores = []

def setupScores():
    print(len(players))
    for i in range(0, len(players)):
        print("trigger")
        playerScores.append({"Aces" : 0,
                     "Twos" : 0,
                     "Threes" : 0,
                     "Fours" : 0,
                     "Fives" : 0,
                     "Sixes" : 0,
                     "DiceTotalsUpper" : 0,
                     "DiceTotalBonus" : 0,
                     "UpperTotal" : 0,
                     "3OfAKind" : 0,
                     "4OfAKind" : 0,
                     "FullHouse" : 0,
                     "SmallStraight" : 0,
                     "LargeStraight" : 0,
                     "Yahtzee" : 0,
                     "Chance" : 0,
                     "LowerTotal" : 0,
                     "YahtzeeBonus" : 0,
                     "GrandTotal" : 0})

setupScores()
print(playerScores)


# def printScoreSheet():
#     for line in lines:
#         print(line + "\n")    
# editScore(1, "Aces", 1)

