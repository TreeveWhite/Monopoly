"""
File that holds the Playermanager Class.
"""

from Player import *
from Dice import *
from SquareClasses import *

class PlayerManager:

    def getPlayers(self, numPlayers, interface):
        players = []
        names = interface.getPlayerNames(numPlayers)
        for player in range(numPlayers):
            name = names[player]
            p = Player(name, 500, [], 0)
            players.append(p)
        return players

    def propertyPlayerOn(self, position, board):
        for place in board:
            if place.position == position:
                return place

    def takeTurn(self, player, board, interface):
        interface.startTurn(player)
        distance = 0
        goPrision = False
        interface.rollDice()
        for roll in range(3):
            result = Dice.roll()
            interface.showDice(result)
            distance += result[0] + result[1]
            if result[0] == result[1] and roll == 2:
                goPrision = True
            elif result[0] == result[1]:
                interface.rollAgain()
                continue
            else:
                break   
                
        if goPrision:
            #send player to prison.
            player.movePlayer(100)
        else:
            player.movePlayer(distance)
            propertyOn = self.propertyPlayerOn(player.position, board)

        if self.checkPayRent(player, board):
            interface.payRent()
        else:
            if interface.wantToBuy(propertyOn):
                if self.playerBuy(player, board):
                    interface.success()
                else:
                    interface.fail()
            else:
                pass

    def playerBuy(self, player, board):
        propertyPositionToBuy = player.position
        propertyClass = self.propertyPlayerOn(propertyPositionToBuy, board)
        """
        print(propertyPositionToBuy)
        print(propertyClass.name)"""

        if player.money >= propertyClass.price:
            propertyClass.ownedBy = player
            player.money -= propertyClass.price
            player.properties.append(propertyClass)
            #propertyClass.prettyPrint()
            return True
        else:
            return False
        
    def checkPayRent(self, player, board):
        propertyOn = self.propertyPlayerOn(player.position, board)
        if propertyOn.ownedBy == None:
            return False
        else:
            player.money -= propertyOn.rent
            return True
