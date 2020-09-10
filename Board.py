from Tile import Tile
from Ship import Ship

class Board:

    __tileArray__ = [] # Private member variable, stores 2d array of tiles as the "board"

    #*****Default Constructor*****
    #Parameters: n/a
    #Returns: n/a
    #Preconditions: n/a
    #Postconditions: A 9x9 board of tiles is created. All of the tiles have water as their item, and false as their attacked status
    def __init__(self):
        for y in range(9):
            tileRow = []
            for x in range(9):
                tileRow = tileRow + [Tile()]
            self.__tileArray__ = self.__tileArray__ +  [tileRow]
    #****************************
    
    #*****Place Ship Method*****
    #Parameters: Direction (up, down, left, right), Ship object (health and name), xCoord (0 - 8), yCoord (0 - 8) ***TOP LEFT IS 0,0!!!***
    #Returns: True (if ship has been placed), False(if ship encountered an issue while being placed)
    #Preconditions: Valid 9x9 board created, the board can have other ships on it already
    #Postconditions: Assuming true, a ship is placed at the correct coordinates in the direction specified
    def placeShip(self, ship):
        direction = ship.direction
        xCoord    = ship.coordinates[0][0]
        yCoord    = ship.coordinates[0][1]
        if (xCoord > 8 or yCoord > 8 or xCoord < 0 or yCoord < 0): # checks to make sure it is a valid coordinate on the board (Cant place a ship at -3, 50)
            raise Exception("Error Invalid X or Y bound to place a ship") 

        if (direction == "up"):     
            if ((yCoord - ship.getHealth()) < 0): #checks to see if the farthest point of the ship will go out of bounds 
                return False                      #(if you try to place a battleship at 0, 0 going up means that it will be going out of bounds, thus this returns false)
            for y in range(ship.getHealth()):
                if (self.__tileArray__[yCoord - y][xCoord].getTileItem() != "water"): #checks that the tiles are empty where the ship goes 
                    return False                                                      #(if a spot is occupied by a different ship this returns false)
            for y in range(ship.getHealth()):   #places the ship in the direction specified
                self.__tileArray__[yCoord - y][xCoord].setTileItem(ship.getName())

        if (direction == "down"):
            if ((ship.getHealth() + yCoord) > 8):
                return False
            for y in range(ship.getHealth()):
                if (self.__tileArray__[yCoord + y][xCoord].getTileItem() != "water"):
                    return False
            for y in range(ship.getHealth()):
                self.__tileArray__[yCoord + y][xCoord].setTileItem(ship.getName())

        if (direction == "left"):
            if ((xCoord - ship.getHealth()) < 0):
                return False
            for x in range(ship.getHealth()):
                if (self.__tileArray__[yCoord][xCoord - x].getTileItem() != "water"):
                    return False
            for x in range(ship.getHealth()):
                self.__tileArray__[yCoord][xCoord - x].setTileItem(ship.getName())

        if (direction == "right"):
            if ((ship.getHealth() + xCoord) > 8):
                return False
            for x in range(ship.getHealth()):
                if (self.__tileArray__[yCoord][xCoord + x].getTileItem() != "water"):
                    return False
            for x in range(ship.getHealth()):
                self.__tileArray__[yCoord][xCoord + x].setTileItem(ship.getName())

        return True #only returns true if the ship was properly placed
    #****************************

    def isValid(self, xCoord, yCoord):
        if (xCoord > 8 or yCoord > 8 or xCoord < 0 or yCoord < 0): #checks to see if it is in bounds
            raise Exception("Error Invalid X or Y bound to attack a tile")
        return(not self.__tileArray__[yCoord][xCoord].getTileAttacked()) #returns true if the tile has not been attacked

    #*****Attack Tile Method*****
    #Parameters: xCoord (0 - 8), yCoord (0 - 8) ***TOP LEFT IS 0,0!!!***
    #Returns: True (if the first time the tile has been attacked), False (if the tile has been attacked before)
    #Preconditions: Valid 9x9 board exists
    #Postconditions: If the tile hasn't been attacked before sets the tiles attacked status to true, if it had been attacked does nothing
    def attackTile(self, xCoord, yCoord):
        if (xCoord > 8 or yCoord > 8 or xCoord < 0 or yCoord < 0): #checks to see if it is in bounds
            raise Exception("Error Invalid X or Y bound to attack a tile")
        if self.__tileArray__[yCoord][xCoord].getTileAttacked():    #checks to see if it has been attacked before
            return False
        self.__tileArray__[yCoord][xCoord].setTileAttacked()    #if it hasn't been attacked sets it to attacked and returns true
        return True
    #****************************

    #*****Get Tile Method*****
    #Parameters: xCoord (0 - 8), yCoord (0 - 8) ***TOP LEFT IS 0,0!!!***
    #Returns: the tile object at that coordinate (contains name and if the tile has been attacked or not)
    #Preconditions: Valid 9x9 board exists
    #Postconditions: n/a
    def getTile(self, xCoord, yCoord):
        if (xCoord > 8 or yCoord > 8 or xCoord < 0 or yCoord < 0): #checks to see if it is in bounds
            raise Exception("Error Invalid X or Y bound to retrieve a tile")
        return self.__tileArray__[yCoord][xCoord]
    #****************************




