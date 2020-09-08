from enum import Enum


# simple ship class which has health and a name

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def nextDirection(self):
        return Direction((self.value + 1) % 4) #cycles through the directions


class Ship:

    def __init__(self, name, direction, length, x, y):  # assigns health and name in default constructor
        self.shipName = name
        self.shipDirection = direction
        self.shipCoordinates = (x, y)
        self.shipLength = length

    def getName(self):
        return self.shipName

    def getHealth(self):
        return self.shipLength

    def damageShip(self):  # damages ship health by 1
        if self.shipLength > 0:
            self.shipLength = self.shipLength - 1

    def isDead(self):  # if health is 0, ship is dead
        if self.shipLength == 0:
            return True
        return False



    def shipCoordinateList(self):
        x, y = self.shipCoordinates
        if self.shipDirection == Direction.UP:
            return [(x, y - i) for i in range(0, self.shipLength)]
        elif self.shipDirection == Direction.LEFT:
            return [(x + i, y) for i in range(0, self.shipLength)]
        elif self.shipDirection == Direction.DOWN:
            return [(x, y + i) for i in range(0, self.shipLength)]
        elif self.shipDirection == Direction.RIGHT:
            return [(x - i, y) for i in range(0, self.shipLength)]
