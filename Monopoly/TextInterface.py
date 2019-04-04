"""
File thats holds the class which controlls all text inputs for the monopoly game.
"""

class TextInterface:

    def showWelcome(self):
        print("Welcome to Monopoly\nThis game took me FUCKING ages to make so please be kind")

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