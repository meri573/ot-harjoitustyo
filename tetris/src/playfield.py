import pygame
from sprites.empty import Empty
from sprites.wall import Wall
from sprites.block import Block


class Playfield:
    def __init__(self, playfield_map, cell_size):
        self.cell_size = cell_size
        self.walls = pygame.sprite.Group()
        self.empty = pygame.sprite.Group()
        self.active_block = pygame.sprite.Group()
        self.locked_blocks = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group()

        self.initialize_sprites(playfield_map)

    def initialize_sprites(self, playfield_map, color=(255, 255, 255)):
        height = len(playfield_map)
        width = len(playfield_map[0])

        for y in range(height):
            for x in range(width):
                cell = playfield_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.empty.add(
                        Empty(normalized_x, normalized_y, self.cell_size))
                elif cell == 1:
                    self.walls.add(
                        Wall(normalized_x, normalized_y, self.cell_size))
                elif cell == 2:
                    self.active_block.add(
                        Block(normalized_x, normalized_y, self.cell_size, color))

        self.all_sprites.add(
            self.walls,
            self.empty,
            self.active_block,
            self.locked_blocks
        )

    def _can_move(self, sprite, delta_x=0, delta_y=0):
        pygame.sprite.move_ip(delta_x, delta_y)

        colliding_walls = pygame.sprite.spritecollide(
            sprite, self.walls, False)
        colliding_locked_blocks = pygame.sprite.spritecollide(
            sprite, self.locked_blocks, False)
        can_move = not colliding_walls and not colliding_locked_blocks

        pygame.sprite.move_ip(-delta_x, -delta_y)

        return can_move

    def _group_can_move(self, group, delta_x=0, delta_y=0):
        for sprite in group:
            boolean_value = self._can_move(sprite, delta_x, delta_y)
            if boolean_value is False:
                break

        return boolean_value

    def move_block(self, sprite, delta_x=0, delta_y=0):
        pygame.sprite.move_ip(delta_x, delta_y)

    def move_group(self, group, delta_x=0, delta_y=0):
        if not self._group_can_move:
            return

        for sprite in group:
            self.move_block(sprite, delta_x, delta_y)
