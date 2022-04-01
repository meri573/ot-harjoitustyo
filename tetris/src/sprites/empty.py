import pygame

class Empty(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, width=0, height=0, color=(0,0,0)):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = pygame.Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y