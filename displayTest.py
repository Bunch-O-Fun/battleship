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
        self.boardHeight = self.cell_size * 2 * board_size + 3 * margin + 15

        self.screen = pygame.display.set_mode((self.boardWidth, self.boardHeight)) #initializes screen
        pygame.display.set_caption('Battleship!') #puts caption on top
        self.screen.fill((47, 62, 216))

    def screenFill(self):

        xCoordinates = ["A", "B", "C", "D", "E", "F", "G", "H"]
        yCoordinates = ["8","7","6","5","4","3","2","1", " "]

        font = pygame.font.SysFont('freesansbold.ttf', 30)

        for y in range(9):
            for x in range(9):
                if x == 0:

                    square = pygame.Rect(x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size)
                    #text = font.render(yCoordinates[y], True, (0,0,0))
                    #textRect = text.get_rect()
                    #square.clamp(textRect)
                    #self.screen.blit(text, textRect)
                    pygame.draw.rect(self.screen, (255, 255, 255, 255), square, 0)



                elif y == 8:
                    square = pygame.Rect(x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, (255, 255, 255, 255), square, 0)

                else:
                    square = pygame.Rect(x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, (255, 255, 255, 255), square, 1)



        buffer = self.margin * 2 + self.board_size * self.cell_size
        for y in range(9):
            for x in range(9):

                if x == 0:
                    square = pygame.Rect(x*self.cell_size, y*self.cell_size + buffer, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, (255, 255, 255, 255), square, 0)

                if y == 8:
                    square = pygame.Rect(x*self.cell_size, y*self.cell_size + buffer, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, (255, 255, 255, 255), square, 0)

                else:
                    square = pygame.Rect(x*self.cell_size, y*self.cell_size + buffer, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, (255, 255, 255, 255), square, 1)

        self.fillCoordinates()

    
    def fillCoordinates(self):

        xCoordinates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        yCoordinates = ['8','7','6','5','4','3','2','1', ' ']
        bottom = 30
        left = 35

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



#Testing environtment for code
#This is where I am teaching myself pygame
#Don't pay much mind



d = Display()
d.screenFill()
#d.fillCoordinates()


running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
