import pygame
pygame.init()
 

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pin-pong")

game = True

clock = pygame.time.Clock()
 

while game:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [320, 0], [330, 450], 5)
 
    pygame.display.flip()
   
    clock.tick(60)

class Chief(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.rect = self.image.get_rect()

from chief import Chief

chiefA = Paddle(WHITE, 10, 100)
chiefA.rect.x = 20
chiefArect.y = 200

chiefB = Paddle(WHITE, 10, 100)
chiefB.rect.x = 670
chiefB.rect.y = 200
 
pygame.quit()