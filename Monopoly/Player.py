"""
File that holds the Player Class.
"""

class Player:
    
    def __init__(self, name, money, properties, position):
        self.name = name
        self.money = money
        self.properties = properties
        self.position = position

    def movePlayer(self, distance, board):
        newDist = (self.position + distance) % len(board)
        self.position = newDist
    
    def playerPassGo(self):
        self.money += 200
