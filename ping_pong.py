import pygame
pygame.init()
 

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pin-pong")


class Chief(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.rect = self.image.get_rect()
        
def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
          self.rect.y = 400
 
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
 
chiefA = Chief(WHITE, 10, 100)
chiefA.rect.x = 20
chiefA.rect.y = 200
 
chiefB = Chief(WHITE, 10, 100)
chiefB.rect.x = 670
chiefB.rect.y = 200

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(chiefA)
all_sprites_list.add(chiefB)

game = True

clock = pygame.time.Clock()

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              game = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: 
                     game=False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)    

    all_sprites_list.update()
 
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    all_sprites_list.draw(screen) 
 
    pygame.display.flip()

    clock.tick(60)

pygame.quit()