import pygame
import sys

class Display:

    water = (21,72,161)
    ship = (102,51,0)
    hit = (255,0,0)
    miss = (235,214,233)
    background = (0,0,0)
    text = (255,255,255)

    def __init__ (self, board_size = 25, cell_size = 20, margin = 15): #constructor of the display, dimensions
        self.board_size = board_size
        self.cell_size = cell_size
        self.margin = margin
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("ComicSans",15) # sets font
        screen_width = 470 #self.cell_size * board_size + 2 * margin # sets width
        self.screen_width = screen_width
        screen_height = 900 #2 * self.cell_size *board_size + 3 * margin #sets heigth
        self.screen_height = screen_height
        screen = pygame.display.set_mode([screen_width, screen_height])
        self.screen = screen
        self.screen.fill((0,0,0))
        pygame.display.set_caption("Battleship!") #name of window
        clock = pygame.time.Clock()


    def input (self,running = True): # user interaction with the display
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #user wnats to quit the game
                Display.close()
            elif event.type == pygame.MOUSEBUTTONDOWN: # when user mouse buttons down
                xcoord, ycoord = pygame.mouse.get_pos()
                ycoord = ycoord % (self.board_size * self.cell_size + self.margin)
                xcoord = (xcoord - self.margin) // self.cell_size
                ycoord = (ycoord - self.margin) // self.cell_size
                if x in range(self.board_size) and y in range(self.board_size):
                    return xcoord, ycoord
        return None, None

    def visual(self):
        white = (255,255,255)
        red = (255,14,14)
        ocean = (52,196,206)
        blockSize = 40
        done = False
        gridtop = []
        for y in range(9):
            gridtop.append([])
            for x in range(9): # this is the top grid
                    rect = pygame.Rect(50 + x*blockSize, y*blockSize + 40, blockSize, blockSize)
                    #pygame.draw.rect(self.screen, white, rect, 1)
                    gridtop[y].append([rect])

        for event in pygame.event.get():
            if event.type ==pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0] // (self.screen_width + self.margin)
                y = pos[1] // (self.screen_height + self.margin)
                gridtop[y][x] = 1 # this indicates a pressed/hit square

        for y in range (9):
            for x in range(9):
                color = ocean
                if gridtop[y][x] == 1:
                    color = red
                pygame.draw.rect(mygame.screen, color, rect, 1)

#---------------------------------- BOTTOM GRID --------------------------------------------#
        buffer = self.margin / 30 + self.board_size * self.cell_size
        for y in range(9): # this is the bottom grid
            for x in range(9):
                square = pygame.Rect(50 + x*blockSize, y*blockSize + buffer, blockSize, blockSize)
                pygame.draw.rect(self.screen, (255, 255, 255, 255), square, 1)
#------------------------------------- END OF VISUAL ---------------------------------------#

    def fillCoordinates(self):
        xCoordinates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        yCoordinates = ['9','8','7','6','5','4','3','2', '1']
        bottom = 75
        left = 55
        black = (0,0,0)
        white = (255, 255, 255)
        font = pygame.font.Font('freesansbold.ttf', 20)
        #for top board Y coordinates
        for y in range(9):
            text = font.render(yCoordinates[y], True, white, black)
            textRect = text.get_rect()
            textRect.bottom = bottom
            textRect.right = 30 # x axis of label
            self.screen.blit(text, textRect)
            bottom = bottom + 40 # distance between characters
        #for top board X coordinates
        for x in range(9):
            text = font.render(xCoordinates[x], True, white, black)
            textRect = text.get_rect()
            textRect.top = 405 # y axis of label
            textRect.left = left
            self.screen.blit(text, textRect)
            left = left + 41 # distance between characters

        #for bot board Y coordinates
        for y in range(9):
            text = font.render(yCoordinates[y], True, white, black)
            textRect = text.get_rect()
            textRect.bottom = bottom + 100 # y axis of label
            textRect.right = 30
            self.screen.blit(text, textRect)
            bottom = bottom + 40 # distance between characters

        left = 55 #reset left coordinate
        # for bot board X coordinates
        for x in range(9):
            text = font.render(xCoordinates[x], True, white, black)
            textRect = text.get_rect()
            textRect.top = 865 # x axis of labels
            textRect.left = left
            self.screen.blit(text, textRect)
            left = left + 41 # distance between characters



mygame = Display()
mygame.visual()
mygame.fillCoordinates()
mygame.input()
running = True
while running:
    pygame.display.flip() # updates the visuals on the board
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # the user wants to quit the game

pygame.quit()
