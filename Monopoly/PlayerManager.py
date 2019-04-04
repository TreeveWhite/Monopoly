"""
File that holds the Playermanager Class.
"""

from Player import *
from Dice import *

class PlayerManager:

    def getPlayers(self, numPlayers, inputInterface):
        players = []
        names = inputInterface.getPlayerNames(numPlayers)
        for player in range(numPlayers):
            name = names[player]
            p = Player(name, 500, [], 0)
            players.append(p)
        return players

    def propertyPlayerOn(self, position, board):
        for place in board:
            if place.position == position:
                return place

    def takeTurn(self, player, board):
        distance = 0
        goPrision = False
        for roll in range(3):
            result = Dice.roll()
            distance += result[0] + result[1]
            if result[0] == result[1] and roll == 2:
                goPrision = True
            elif result[0] == result[1]:
                continue
            else:
                break   
                
        if goPrision:
            #send player to prison.
            player.movePlayer(100)
        else:
            player.movePlayer(distance)
            propertyOn = self.propertyPlayerOn(player.position, board)