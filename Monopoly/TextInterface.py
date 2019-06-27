"""
File thats holds the class which controlls all text inputs for the monopoly game.
"""

class TextInterface:

    def showWelcome(self):
        print("Welcome to Monopoly\nThis game took me ages to make so please be kind\nYou start with £500")

    def getNumPlayers(self):
        numPlayers = int(input("How many Players?"))
        return numPlayers
    
    def getPlayerNames(self, numPlayers):
        playersNames = []
        for player in range(numPlayers):
            playersNames.append(input("Enter Player {} Name:    ".format(player+1)))
        return playersNames
    
    def showDetails(self, player, board):
        p = []
        for prop in player.properties:
            p.append(prop.name)
        print("\n{} has £{}\nProperties: {}\nPosition: {}\n".format(player.name, player.money, p, board[player.position].name))
    
    def wantToBuy(self, propertyGiven):
        choice = input("Do You wish to buy {} for £{}? Y/N".format(propertyGiven.name, propertyGiven.price)).lower()
        if choice == "y":
            return True
        else:
            return False
    
    def success(self):
        print("Success!")

    def fail(self):
        print("Sorry You Cant Do that!")
    
    def rollDice(self):
        input("Roll Dice...")

    def rollAgain(self):
        input("Double! Roll Again")
    
    def showDice(self, result):
        print("You rolled a {} and a {}!".format(result[0], result[1]))
        input("Continue...")
    
    def startTurn(self, player):
        print("It is {} Turn".format(player.name))
        input("Continue...")
    
    def wantToBuyHouses(self, propertyOn):
        choice = input("Do You want to buy houses for {}".format(propertyOn.name))
        return choice
    
    def howManyHouses(self, propertyOn):
        choice = input("How many Houses do you want to buy?\nThey cost {} Each".format(propertyOn.buildingCost))
        return choice
    
    def notEnoughMoney(self):
        print("You dont have enough money for this!")
    
    def maxNumHouses(self):
        print("You have the max num of Houses on this property!")
    
    def payRent(self, propertyOn):
        print("You have to pay rent! The Rent is £{}".format(propertyOn.rent[propertyOn.numHouses]))
    
    def inPrison(self, propertyOn, player):
        print("You have been sent to Prison for {} Rolls".format(propertyOn.prisoners[player]))
    
    def showCard(self, card):
        print(card)

    def currentPosition(self, position):
        print("\nYou are on {}".format(position))
