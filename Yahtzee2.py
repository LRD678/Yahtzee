"""
	Description: Yahtzee 2 :(
	Author: Landen Dwyer
	Date of first edit: Wed Jan  7 12:24:20 2026
"""

import random

players = []

playerScores = []

def setup():
    # Get the amt of players
    amtOfPlayers = int(input("How many players are playing?"))
    
    # Get player names and setup the scoring dict
    for i in range(0, amtOfPlayers):
        players.append(input("Insert player name"))
        playerScores.append({"Aces" : 0,
                     "Twos" : 0,
                     "Threes" : 0,
                     "Fours" : 0,
                     "Fives" : 0,
                     "Sixes" : 0,
                     "DiceTotalUpper" : 0,
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

setup()

def gameLoop():
    # Check if the game is still playable or if we move onto totaling
    while scoresAvilable():
        
        # Loop through the players (turn cycle bsaically)
        for player in players:
            
            # Roll initial 5 dice for the player
            dice = [random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)]
            
            heldDice = []
            
            # Go through your 3 rerolls
            for i in range(0, 3):

                # Reset your dice 
                amtOfDice = len(dice)
                dice = []
                for i in range(0, amtOfDice):
                    dice.append(random.randint(1, 6))
                
                # Reset rolls done which tells if the player has inputed y and is done holding dice
                rollsDone = False
                
                # While there is still dice to roll and the player has not chose to move on
                while len(dice) > 0 and rollsDone == False:
                    
                    # Offer input to see what the player wants to do
                    print("Dice" + str(dice))
                    print("Held" + str(heldDice))
                    inp = input('Type the num of each roll you would like to hold or y to move on')
                    
                    # 'y' was inputed to break the loop
                    if inp == "y":
                        rollsDone = True
                        print("rollsdone")
                        
                    # add the chosen roll to held dice and remove it from the rolled dice    
                    elif int(inp) in [1, 2, 3, 4, 5]:
                        heldDice.append(dice.pop(int(inp)-1))

                    

def scoresAvilable():
    # Loop through the scores and check if any of them are still 0 if they are then there is still scores to be scored
    for player in playerScores:
        for score in player.values():
            if score == 0:
                return True
    return False

gameLoop()