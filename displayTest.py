import pygame

#class Display:

WHITE = (255, 255, 255, 255)



#Testing environtment for code
#This is where I am teaching myself pygame
#Don't pay much mind

backgroundColor = (47, 62, 216)
width = 400
height = 900

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Battleship!')
screen.fill(backgroundColor)

blockSize = 50
for y in range(8):
    for x in range(8):
        square = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, WHITE, square, 1)


running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
