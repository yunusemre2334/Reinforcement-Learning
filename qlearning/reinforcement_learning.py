import pygame 
import random 

WIDTH = 360
HEIGHT = 360 
FPS = 30 

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RL Game")
clock = pygame.time.Clock()

running = True

while running:
    # keep loop running at the right speed
    clock.tick(FPS)

    # process input

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # update
            
    # draw / render(show)
    screen.fill(GREEN)

    # after drawing
    pygame.display.flip()

pygame.quit()
