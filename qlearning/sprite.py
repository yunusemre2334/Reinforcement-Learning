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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.y_speed = 5
        
    def update(self):
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT -200:
            self.y_speed = -5
        
        if self.rect.top < 0:
            self.y_speed = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RL Game")
clock = pygame.time.Clock()

all_sprite = pygame.sprite.Group()
player = Player()
all_sprite.add(player)


running = True

while running:
    # keep loop running at the right speed
    clock.tick(FPS)

    # process input

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # update
    all_sprite.update()
            
    # draw / render(show)
    screen.fill(GREEN)
    all_sprite.draw(screen)

    # after drawing
    pygame.display.flip()

pygame.quit()
