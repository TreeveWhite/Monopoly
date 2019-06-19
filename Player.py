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
        print(self.position, len(board), distance)
        if self.position + distance < len(board):
            self.position += distance
        elif self.position + distance > len(board):
            newdist = (self.position + distance) - len(board)
            self.position = newdist
        print(self.position)

    def playerPassGo(self):
        self.money += 200
