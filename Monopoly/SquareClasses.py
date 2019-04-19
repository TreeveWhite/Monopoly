"""
All the classes for the Squarres / positions on board.
"""

import random

class Square:

    def __init__(self, name, position):
        self.name = name
        self.position = position

class Property(Square):

    def __init__(self, name, position, price, rent, morgage, buildingCost):
        self.price = price
        self.rent = rent
        self.morgage = morgage
        self.buildingCost = buildingCost
        self.ownedBy = None
        self.numHouses = 0

        Square.__init__(self, name, position)
    
    def addHouse(self):
        self.numHouses += 1
        
    def prettyPrint(self):
        print("Proterty -- {}\nPrice -- {}\nRent -- {}\nPosition -- {}\nMorgage -- {}\nBuilding Cost -- {}\nOwned By -- {}\n\n".format(self.name, 
                                                                                                                    self.price,
                                                                                                                    self.rent[0],
                                                                                                                    self.position,
                                                                                                                    self.morgage,
                                                                                                                    self.buildingCost,
                                                                                                                    self.ownedBy))

    

class GoSquare(Square):
    
    def __init__(self, name, position):
        self.name = "Go"
        self.position = 0

    def prettyPrint(self):
        print("GO SQUARE\nGAIN £200 WHEN CROSSED\n\n")

class Jail:
    
    def __init__(self, name, position):
        self.name = "Jail"
        self.prisoners = {}
        self.position = position

class ChanceCard:

    def __init__(self, name, position):
        self.name = "Chance Card"
        self.position = position
    
    def getCard(self):
        with open("ChanceCards.txt", "r") as file:
            cards = []
            for line in file:
                cards.append(line.strip())
        choice = random.randint(0, len(cards)-1)
        card = cards[choice]
        return card

    def prettyPrint(self):
        print("Property -- Chance card\nPosition -- {}".format(self.position))
        
class ComunityChest:

    def __init__(self, name, position):
        self.name = "Comunity Chest"
        self.position = position
    
    def prettyPrint(self):
        print("Property -- Comunity Chest\nPosition -- {}".format(self.position))

class FreeParking:

    def __init__(self, name, position):
        self.name = "Free Parking"
        self.position = position
    
    def prettyPrint(self):
        print("Property -- Free Parking\nPosition -- {}".format(self.position))

class GoToJail:

    def __init__(self, name, position):
        self.name = "Go To Jail"
        self.position = position
    
    def prettyPrint(self):
        print("Property -- Go To Jail\nPosition -- {}".format(self.position))