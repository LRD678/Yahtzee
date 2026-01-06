"""
	Description: Yahtzee
	Author: Landen Dwyer
	Date of first edit: Mon Jan  5 12:19:08 2026
"""

import random


players = []

validYNInputs = ["y", "n"]

gameState = {"Setup" : 0,
             "Rolling" : 0,
             "Scoring" : 0
             }

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
    players = []
    
    # Get all of the player names into the dictionary
    for player in range(0, amountOfPlayers):
        players.append(input(f"Insert player {player+1}'s name\n"))
        
    # Check if names are correct and finish game setup
    if validInput(f"The players are {players}, can I proceed? (y/n)\n", validYNInputs) == "y":
        players = random.shuffle(players)
        print("confirmed")
        gameState["Setup"] = 1   

# Setup the players
while gameState["Setup"] == 0:
    setupPlayers()