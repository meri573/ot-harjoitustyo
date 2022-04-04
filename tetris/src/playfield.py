import pygame
from sprites.empty import Empty
from sprites.wall import Wall

class Playfield:
    def __init__(self, playfield_map, cell_size):
        self.cell_size = cell_size
        self.walls = pygame.sprite.Group()
        self.empty = pygame.sprite.Group()
        self.active_block = pygame.sprite.Group()
        self.locked_blocks = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group()




    def _initialize_sprites(self, playfield_map):
        height = len(playfield_map)
        width = len(playfield_map[0])

        for y in range(height):
            for x in range(width):
                cell = playfield_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.empty.add(Empty(normalized_x, normalized_y, width, height))
                elif cell == 1:
                    self.walls.add(Wall(normalized_x, normalized_y, width, height))

        self.all_sprites.add(
            self.walls,
            self.empty,
            self.active_block,
            self.locked_blocks
            )