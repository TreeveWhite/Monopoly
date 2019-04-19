"""
File that holds the Playermanager Class.
"""

from Player import *
from Dice import *
from SquareClasses import *
from AnalyseCard import *

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
        threeDouble = False

        if self.playerInPrison(player, board):
            interface.inPrison(self.propertyPlayerOn(player.position, board), player)
            return None
            
        interface.rollDice()
        for roll in range(3):
            result = Dice.roll()
            interface.showDice(result)
            distance += result[0] + result[1]
            if result[0] == result[1] and roll == 2:
                threeDouble = True
            elif result[0] == result[1]:
                interface.rollAgain()
                continue
            else:
                break   
                
        if threeDouble:
            self.sendToPrison(player, interface, board)
            return None
        else:
            player.movePlayer(distance)
            propertyOn = self.propertyPlayerOn(player.position, board)
        if propertyOn.name == "Chance Card":
            card = propertyOn.getCard()
            interface.showCard(card)
            AnaliseChance.Analise(card, player)
            return None
        elif propertyOn.name == "Comunity Chest":
            return None
        elif propertyOn.name == "Jail":
            return None
        elif propertyOn.name == "Go":
            return None
        elif propertyOn.name == "Free Parking":
            return None
        elif propertyOn.name == "Go To Jail":
            self.sendToPrison(player, interface, board)
            return None

        if self.checkPayRent(player, board):
            interface.payRent(propertyOn)
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

        if player.money >= propertyClass.price:
            propertyClass.ownedBy = player
            player.money -= propertyClass.price
            player.properties.append(propertyClass)
            return True
        else:
            return False
        
    def checkPayRent(self, player, board):
        propertyOn = self.propertyPlayerOn(player.position, board)
        if propertyOn.ownedBy == None:
            return False
        elif propertyOn.ownedBy == player:
            return True
        else:
            player.money -= propertyOn.rent[propertyOn.numHouses]
            propertyOn.ownedBy.money += propertyOn.rent[propertyOn.numHouses]
            return True
    
    def buyHouse(self, player, board, interface):
        interface.wnatToBuyHouses()
        propertyOn = self.propertyPlayerOn(player.position, board)
        if propertyOn.numHouses != 5:
            numHouses = interface.howManyHouses()
            if player.money - (propertyOn.buildingCost * numHouses) >= 0:
                for i in range(numHouses):
                    propertyOn.buyHouse()
            else:
                interface.notEnoughMoney()
        else:
            interface.maxNumHouses()
    
    def sendToPrison(self, player, interface, board):
        player.position = 6
        self.propertyPlayerOn(player.position, board).prisoners[player] = 3
        interface.inPrison(self.propertyPlayerOn(player.position, board), player)
    
    def playerInPrison(self, player, board):
        if self.propertyPlayerOn(player.position, board).name == "Prison":
            self.propertyPlayerOn(player.position, board).prisoners[player] -= 1
            if self.propertyPlayerOn(player.position, board).prisoners[player] <= 0:
                return False
            else:
                return True
        else:
            return False