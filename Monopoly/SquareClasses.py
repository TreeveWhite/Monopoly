"""
All the classes for the Squarres / positions on board.
"""


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

        Square.__init__(self, name, position)
        
    def prettyPrint(self):
        print("Proterty -- {}\nPrice -- {}\nRent -- {}\nPosition -- {}\nMorgage -- {}\nBuilding Cost -- {}\nOwned By -- {}\n\n".format(self.name, 
                                                                                                                    self.price,
                                                                                                                    self.rent[0],
                                                                                                                    self.position,
                                                                                                                    self.morgage,
                                                                                                                    self.buildingCost,
                                                                                                                    self.ownedBy))

class Utility(Square):

    def __init__(self, name, position, price, rent, morgage):
        self.price = price
        self.rent = rent
        self.morgage = morgage
        self.ownedBy = None
        Square.__init__(self, name, position)

    def prettyPrint(self):
        print("Proterty -- {}\nPrice -- {}\nRent -- {}\nPosition -- {}\nMorgage -- {}\n\n".format(self.name, 
                                                                                                self.price,
                                                                                                self.rent[0],
                                                                                                self.position,
                                                                                                self.morgage))

class SpecialCard(Square):

    def __init__(self, name, position):
        Square.__init__(self, name, position)


class GoSquare(Square):
    
    def __init__(self, name, position):
        self.name = "Go"
        self.position = 0

    def prettyPrint(self):
        print("GO SQUARE\nGAIN £200 WHEN CROSSED\n\n")
