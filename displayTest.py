import pygame


class Display:

    def __init__(self, cell_size = 30, board_size = 8, margin = 15):
        self.board_size = board_size
        self.cell_size = cell_size
        self.margin = margin

        pygame.init() #initializes pygame
        pygame.font.init() #initializes the pygame font
        self.font = pygame.font.SysFont("Comic Sans", 16)

        self.boardWidth = self.cell_size * board_size + 2 * margin
        self.boardHeight = self.cell_size * 2 * board_size + 3 * margin

        self.screen = pygame.display.set_mode((self.boardWidth, self.boardHeight)) #initializes screen
        pygame.display.set_caption('Battleship!') #puts caption on top
        self.screen.fill((47, 62, 216))

    def screenFill(self):

        water = (0, 0, 255) #blue
        ship = (128, 128, 128) #gray
        miss = (255, 255, 255) #white
        border = (255, 255, 255)
        hit =  (255, 0, 0) #red
        buffer = 0

        for y in range(9):
            for x in range(9):
                if x == 0 or y == 8:

                    self.drawSquare(x, y, border, buffer)

                else:

                    self.drawSquare(x, y, water, buffer)

        buffer = self.margin * 2 + self.board_size * self.cell_size
        for y in range(9):
            for x in range(9):

                if x == 0 or y == 8:
                    self.drawSquare(x, y, border, buffer)
                else:
                    self.drawSquare(x, y, water, buffer)

        self.fillCoordinates()


    def drawSquare(self, x, y, color, buffer):
        square = pygame.Rect(x*self.cell_size, y*self.cell_size + buffer, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, color, square, 0)

    def fillCoordinates(self):

        xCoordinates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        yCoordinates = ['8','7','6','5','4','3','2','1', ' ']
        bottom = 30
        left = 30

        black = (0,0,0)
        white = (255, 255, 255)
        font = pygame.font.Font('freesansbold.ttf', 20)

        #for top board Y coordinates
        for y in range(8):
            text = font.render(yCoordinates[y], True, black, white)
            textRect = text.get_rect()
            textRect.bottom = bottom
            textRect.right = 30
            self.screen.blit(text, textRect)
            bottom = bottom + 30
        #for top board X coordinates
        for x in range(8):
            text = font.render(xCoordinates[x], True, black, white)
            textRect = text.get_rect()
            textRect.top = 240
            textRect.left = left
            self.screen.blit(text, textRect)
            left = left + 30

        #for top board Y coordinates
        for y in range(8):
            text = font.render(yCoordinates[y], True, black, white)
            textRect = text.get_rect()
            textRect.bottom = bottom + 30
            textRect.right = 30
            self.screen.blit(text, textRect)
            bottom = bottom + 30

        left = 35 #reset left coordinate
        for x in range(8):
            text = font.render(xCoordinates[x], True, black, white)
            textRect = text.get_rect()
            textRect.top = 510
            textRect.left = left
            self.screen.blit(text, textRect)
            left = left + 30

    def result(self, winner):

        black = (0,0,0)
        red = (255, 0, 0)
        font = pygame.font.Font('freesansbold.ttf', 50)

        if winner == True:
            text = font.render('You Win!', True, black, red)
            textRect = text.get_rect()
            textRect.center = (self.boardWidth // 2, self.boardHeight // 2)
            self.screen.blit(text, textRect)

        else:
            text = font.render('You Lose!', True, black, red)
            textRect = text.get_rect()
            textRect.center = (self.boardWidth // 2, self.boardHeight // 2)
            self.screen.blit(text, textRect)

    def getInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #user wnats to quit the game
                Display.close()
            elif event.type == pygame.MOUSEBUTTONDOWN: # when user mouse buttons down
                pos = pygame.mouse.get_pos()
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                self.grid[row][column] = 1 #this indicates a pressed/hit square

    def askUserCoordinates(self):
        validXCoordinate = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        validYCoordinate = ['1','2','3','4','5','6','7','8','9']

        x = input("Enter an X coordinate (Letters A-I):")
        while not x in validXCoordinate:
            x = input("Error! Enter an X coordinate (Letters A-I):")

        y = input("Enter an Y coordinate (Numbers 1-9):")
        while not y in validYCoordinate:
            y = input("Error! Enter an Y coordinate (Letters 1-9):")

        (x, y) = self.turnCoordinatesIntoInts(x, y)

        return x, y

    #helper function of askUserCoordinates
    def turnCoordinatesIntoInts(self, x, y):
        xCoordinates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']


        yInt = int(y)

        for i in range(9):
            if xCoordinates[i] == x:
                xInt = i+1
                break

        return xInt, yInt




#Testing environtment for code
#This is where I am teaching myself pygame
#Don't pay much mind

d = Display()
d.screenFill()
(x,y) = d.askUserCoordinates()

print(x, y)

running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type ==pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            print(pos)
            d.changeTileColor(x,y)


pygame.quit()
