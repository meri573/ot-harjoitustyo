import pygame


class Empty(pygame.sprite.Sprite):
    def __init__(self, normalized_x=0, normalized_y=0, cell_size=50, color=(200, 200, 200)):
        super().__init__()

        self.cell_size = cell_size

        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = normalized_x
        self.rect.y = normalized_y
