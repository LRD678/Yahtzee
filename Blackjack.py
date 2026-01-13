"""
	Description: Blackjack
	Author: Landen Dwyer
	Date of first edit: Thu Jan  8 13:33:35 2026
"""

import random

# EXAMPLES (stuff I couldn't fit into my project)

# Example Variables

exampleSet = {100, 200, 300}
exampleDict = {'Landen' : 3, 'Marco' : 4, 'Sarim' : 5.0}
listOfLists = [["Landen", "Marco"], [3, 6, 7]]

# Example Functions

def getIdxOfCharInString(givenChar, string):
    try:
        for characterIdx in range(0, len(string)):
            if givenChar == string[characterIdx]:
                return characterIdx
    except:
        print("Something went wrong!")
        
def getFirst3CharOfString(string):
    return string[:3]

def writeFile():
    file1 = open("MyFile.txt","a")
    file1.write("Hello class this is a string that will be saved to a file. All of this text will be on one really long line")
    file1.close()

def readFile(givenFile):
    givenFile.open()
    reading = givenFile.read()
    givenFile.close()
    return reading

def lockStep():
    total = 0
    list1 = [1, 2, 3]
    list2 = [6, 7, 8]
    for i in range(0, len(list1)):
            total += (list1[i] + list2[i])
    return total

assert lockStep() == 27

# GAME PORTION

playersTurn = True
gameOver = False

# Hands

playerHand = []
dealerHand = []
hiddenDealerHand = []


def drawACard():
    
    # Choose a random card from the deck
    targetCard = random.choice(deck)
    
    # Remove that card from the deck
    deck.remove(targetCard)
    
    # Return the card
    return targetCard

def checkCard(givenHand, givenCard):
    
    # Loop through given hand
    for card in givenHand:
        
        # Check if the hand has the given card
        if card[1] == givenCard:
            return True

    return False

def evalHand(givenHand):
    
    total = 0
    
    # Iterate and score the given hand
    for card in givenHand:
        
        match card[1]:
            # Score the face value of the card if its 2-10
            case "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10":
                total += int(card[1])
                
            # Score as 10 points
            case "J" | "Q" | "K":
                total += 10
            
            # Score as an 11
            case "A": 
                total += 11
    # If we busted and we have an ace return it as the ace being 1
    if total > 21 and checkCard(givenHand, "A"):
        total -= 10
        
    return total

def shouldDealerHit():
    
    # Hit if our hand is worth less then 17 or if its greater than/equal to 17 but we need to have an ace
    if evalHand(dealerHand) < 17:
        return True
    
    elif evalHand(dealerHand) >= 17 and checkCard(dealerHand, "A"):
        return True
    
    else:
        return False

deck = []

    
# The decks guides
suites = ["HEARTS", "SPADES", "CLUBS", "DIAMONDS"]
numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Loop through and create 52 cards
for suite in suites:
    for number in numbers:
        deck.append((suite, number))

# Shuffle the deck
random.shuffle(deck)

# Player draws 2 and dealer draws 1 visible and 1 hidden

playerHand.append(drawACard())
playerHand.append(drawACard())
dealerHand.append(drawACard())
hiddenDealerHand.append(drawACard())

print(f"DEALER HAND: {dealerHand} + 1 hidden card")
print(f"YOUR HAND: {playerHand}")

# The player turn

while playersTurn: 
    
    # Every loop check if the players hand is worth more then 21
    if evalHand(playerHand) > 21:
        
        # End the game and the players turn
        playersTurn = False
        gameOver = True
        print(f"Your hand is worth {evalHand(playerHand)} which is over 21! You busted!")
    
    else:
        
        # Ask if player wants to hit or stand
        inp = input("CHOOSE TO HIT (h) OR STAND (s): ")
        
        if inp == "h":
            
            # Draw a card
            playerHand.append(drawACard())
            print(f"DEALER HAND: {dealerHand} + 1 hidden card")
            print(f"YOUR HAND: {playerHand}")
    
        if inp == "s":
            
            # End the players turn
            playersTurn = False

# Do the dealers turn only if the player hasnt lost already

if gameOver == False:
    
    # Dealer draws their hidden card
    dealerHand.append(hiddenDealerHand[0])
    hiddenDealerHand.pop(0)
    print(f"DEALER HAND: {dealerHand}")
    print(f"YOUR HAND: {playerHand}")
    
    # While the dealer should hit and the total of the dealers hand is under 21
    while shouldDealerHit() and evalHand(dealerHand) < 21:
        
        # Draw a card
        dealerHand.append(drawACard())
        print(f"DEALER HAND: {dealerHand}")
        print(f"YOUR HAND: {playerHand}")

    # After the while if the dealers hand is bigger then players and under or equal to 21 the dealer wins
    # otherwise the player wins
    if evalHand(dealerHand) > evalHand(playerHand) and evalHand(dealerHand) <= 21:
        print("You lost!")
    else: 
        print("You win!")