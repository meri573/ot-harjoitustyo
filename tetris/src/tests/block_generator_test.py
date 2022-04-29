import unittest
import pygame

from game_logic.block_generator import BlockGenerator

blocks = [[1, 2]]


class StubPlayfield:
    def __init__(self):
        self.cell_size = 1
        #self.x = 0
        #self.y = 0
        self.next_block = pygame.sprite.Group()
        self.active_block = pygame.sprite.Group()

    def move_group(self, group, delta_x, delta_y):
        for block_sprite in group:
            self.move_block(block_sprite, delta_x, delta_y)

    def move_block(self, block_sprite, delta_x, delta_y):
        block_sprite.rect.move_ip(delta_x, delta_y)

    def initialize_sprites(self, one, two):
        if one == 1 and two == 2:
            self.next_block.add(StubBlock())


class StubBlock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.cell_size = 1
        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class TestBlockGenerator(unittest.TestCase):
    def setUp(self):
        playfield = StubPlayfield()
        self.block_generator = BlockGenerator(playfield, blocks)

    def test_if_move_to_spawnpoint_with_no_sprites_errors(self):
        self.block_generator._move_to_spawnpoint()

    def test_move_to_spawnpoint(self):
        self.block_generator._playfield.next_block.add(StubBlock())
        self.block_generator._move_to_spawnpoint()
        for block_sprite in self.block_generator._playfield.next_block:
            self.assertEqual(block_sprite.rect.x, -
                             self.block_generator.delta_x)
            self.assertEqual(block_sprite.rect.y, -
                             self.block_generator.delta_y)

    def test_move_from_next_block_to_active(self):
        self.block_generator._playfield.next_block.add(StubBlock())
        self.block_generator._move_from_next_block_to_active()
        self.assertEqual(len(self.block_generator._playfield.next_block), 0)
        self.assertEqual(len(self.block_generator._playfield.active_block), 1)

    def test_create_random_block(self):
        self.block_generator.create_random_block()
        self.assertEqual(len(self.block_generator._playfield.next_block), 1)

    def test_move_to_next_block_area(self):
        self.block_generator._playfield.next_block.add(StubBlock())
        self.block_generator._move_to_next_block_area()
        for block_sprite in self.block_generator._playfield.next_block:
            self.assertEqual(block_sprite.rect.x, self.block_generator.delta_x)
            self.assertEqual(block_sprite.rect.y, self.block_generator.delta_y)

    def test_create_block(self):
        self.block_generator.create_block()
        self.assertEqual(len(self.block_generator._playfield.next_block), 1)
