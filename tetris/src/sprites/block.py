import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, normalized_x, normalized_y, cell_size, color, pivot_point):
        super().__init__()

        self.cell_size = cell_size

        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.image.fill(color)

        self.pivot_point = pivot_point

        self.offset_vector = pygame.Vector2()
        self.offset_vector.x = (normalized_x + 0.5 *
                                self.cell_size) - self.pivot_point[0]
        self.offset_vector.y = (normalized_y + 0.5 *
                                self.cell_size) - self.pivot_point[1]

        self.rect = self.image.get_rect()
        self.rect.x = normalized_x
        self.rect.y = normalized_y
