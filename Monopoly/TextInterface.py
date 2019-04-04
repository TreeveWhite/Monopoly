"""
File thats holds the class which controlls all text inputs for the monopoly game.
"""

class TextInterface:

    def showWelcome(self):
        print("Welcome to Monopoly\nThis game took me FUCKING ages to make so please be kind\nYou start with £500")

    def getNumPlayers(self):
        numPlayers = int(input("How many Players?"))
        return numPlayers
    
    def getPlayerNames(self, numPlayers):
        playersNames = []
        for player in range(numPlayers):
            playersNames.append(input("Enter Player {} Name:    ".format(player+1)))
        return playersNames
    
    def showDetails(self, player):
        print("{} has £{}\nProperties: {}\nPosition: {}".format(player.name, player.money, player.properties, player.position))
    
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
