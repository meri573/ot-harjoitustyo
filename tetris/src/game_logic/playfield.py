import pygame
from sprites.empty import Empty
from sprites.wall import Wall
from sprites.block import Block


class Playfield:
    def __init__(self, playfield_map, cell_size, pivot_point):
        self.cell_size = cell_size
        self.pivot_point = pivot_point

        self.walls = pygame.sprite.Group()
        self.empty = pygame.sprite.Group()
        self.active_block = pygame.sprite.Group()
        self.locked_blocks = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group()

        self.initialize_sprites(playfield_map)

    def initialize_sprites(self, playfield_map, color=(255, 255, 255)):
        height = len(playfield_map)
        self.width = len(playfield_map[0])

        for y_index in range(height):
            for x_index in range(self.width):
                cell = playfield_map[y_index][x_index]
                normalized_x = x_index * self.cell_size
                normalized_y = y_index * self.cell_size

                if cell == 0:
                    self.empty.add(
                        Empty(normalized_x, normalized_y, self.cell_size))
                elif cell == 1:
                    self.walls.add(
                        Wall(normalized_x, normalized_y, self.cell_size))
                elif cell == 2:
                    self.active_block.add(
                        Block(normalized_x, normalized_y, self.cell_size, color, self.pivot_point))

        self.all_sprites.add(
            self.walls,
            self.empty,
            self.active_block,
            self.locked_blocks
        )

    def _can_move(self, block_sprite, delta_x=0, delta_y=0):
        block_sprite.rect.move_ip(delta_x, delta_y)

        colliding_walls = pygame.sprite.spritecollide(
            block_sprite, self.walls, False)
        colliding_locked_blocks = pygame.sprite.spritecollide(
            block_sprite, self.locked_blocks, False)
        can_move = not colliding_walls and not colliding_locked_blocks

        block_sprite.rect.move_ip(-delta_x, -delta_y)

        return can_move

    def _group_can_move(self, group, delta_x=0, delta_y=0):
        for block_sprite in group:
            if self._can_move(block_sprite, delta_x, delta_y) is False:
                return False

        return True

    def move_block(self, block_sprite, delta_x=0, delta_y=0):
        block_sprite.rect.move_ip(delta_x, delta_y)

    def move_group(self, group, delta_x=0, delta_y=0):
        if self._group_can_move(group, delta_x, delta_y):
            for block_sprite in group:
                self.move_block(block_sprite, delta_x, delta_y)

    def move_active_block_to_locked(self):
        self.locked_blocks.add(self.active_block)
        self.active_block.remove(self.active_block)

    def can_move_down(self):
        return self._group_can_move(self.active_block, 0, self.cell_size)

    def start_locking(self):

        coordinates = self._get_active_block_y_coordinates()

        self.move_active_block_to_locked()

        lines_removed_y = self._remove_full_lines(coordinates)
        if len(lines_removed_y) > 0:
            self._move_remaining_lines_down(lines_removed_y)
        return len(lines_removed_y)

    def _get_active_block_y_coordinates(self):
        block_y_coordinates = []
        for block_sprite in pygame.sprite.Group.sprites(self.active_block):
            block_y_coordinates.append(block_sprite.rect.y)
        return set(block_y_coordinates)

    # (probably) bad code alert !!!

    def _remove_full_lines(self, coordinates):
        lines_removed_y = []

        for y_coordinate in coordinates:
            sprite_list = []
            for block_sprite in pygame.sprite.Group.sprites(self.locked_blocks):
                if block_sprite.rect.y == y_coordinate:
                    sprite_list.append(block_sprite)

            if len(sprite_list) == self.width - 2:
                lines_removed_y.append(sprite_list[0].rect.y)
                for block_sprite in sprite_list:
                    pygame.sprite.Sprite.kill(block_sprite)
        return lines_removed_y

    def _move_remaining_lines_down(self, lines_removed_y):
        for block_sprite in self.locked_blocks:
            if block_sprite.rect.y < min(lines_removed_y):
                self.move_block(block_sprite, 0, len(
                    lines_removed_y) * self.cell_size)

            # bad code alert
            # can causes issues when clearing more than 5 lines at once but should work for 4
            elif block_sprite.rect.y < max(lines_removed_y):
                for y_coordinate in lines_removed_y:
                    if block_sprite.rect.y < y_coordinate:
                        self.move_block(block_sprite, 0, 1 * self.cell_size)

    def rotate_active_block(self, deg):

        if self._can_rotate(self.active_block, deg):
            for block_sprite in self.active_block:
                rotated_vector = block_sprite.offset_vector.rotate(deg)
                delta_x = -block_sprite.offset_vector.x + rotated_vector.x
                delta_y = -block_sprite.offset_vector.y + rotated_vector.y
                self.move_block(block_sprite, delta_x, delta_y)
                block_sprite.offset_vector = rotated_vector

    def _can_rotate(self, group, deg):
        for block_sprite in group:
            rotated_vector = block_sprite.offset_vector.rotate(deg)
            delta_x = -block_sprite.offset_vector.x + rotated_vector.x
            delta_y = -block_sprite.offset_vector.y + rotated_vector.y
            if not self._can_move(block_sprite, delta_x, delta_y):
                return False
        return True

    def check_if_active_block_inside_locked_block(self):
        for sprite_block in self.active_block:
            if pygame.sprite.spritecollideany(sprite_block, self.locked_blocks) is not None:
                return True
        return False
