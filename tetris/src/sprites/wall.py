import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, cell_size=50, color=(100,100,100)):
        super().__init__()

        self.cell_size = cell_size

        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y