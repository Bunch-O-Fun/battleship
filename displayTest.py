import pygame

class Display:

    def __init__(self, cell_size = 50, board_size = 8, margin = 25):
        self.board_size = board_size
        self.cell_size = cell_size
        self.margin = margin

        pygame.init() #initializes pygame
        pygame.font.init() #initializes the pygame font
        self.font = pygame.font.SysFont("Comic Sans", 16)

        boardWidth = self.cell_size * board_size + 2 * margin
        boardHeight = self.cell_size * 2 * board_size + 3 * margin

        self.screen = pygame.display.set_mode((boardWidth, boardHeight)) #initializes screen
        pygame.display.set_caption('Battleship!') #puts caption on top
        self.screen.fill((47, 62, 216))

    def screenFill(self):

        for y in range(8):
            for x in range(8):
                square = pygame.Rect(50 + x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (255, 255, 255, 255), square, 1)


        buffer = self.margin * 2 + self.board_size * self.cell_size
        for y in range(8):
            for x in range(8):
                square = pygame.Rect(50 + x*self.cell_size, y*self.cell_size + buffer, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (255, 255, 255, 255), square, 1)



#Testing environtment for code
#This is where I am teaching myself pygame
#Don't pay much mind



d = Display()
d.screenFill()


running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
