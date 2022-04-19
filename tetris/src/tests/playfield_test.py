import pygame
import unittest
from playfield import Playfield
from block_generator import BlockGenerator
from sprites.block import Block

PLAYFIELD_MAP = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

TEST_BLOCK_T = ([["x", "x", "x", "x", 2, 2, 2, "x", "x", "x", "x", "x"],
                ["x", "x", "x", "x", "x", 2, "x", "x", "x", "x", "x", "x"]], (153, 51, 255))

BLOCKS = [TEST_BLOCK_T]

CELL_SIZE = 45


class TestPlayfield(unittest.TestCase):
    def setUp(self):
        self.playfield = Playfield(PLAYFIELD_MAP, CELL_SIZE)
        self.block_generator = BlockGenerator(self.playfield, BLOCKS)

    def create_sprite(self, x, y, cell_size):
        return Block(x, y, cell_size)

    def test_wall_created_in_correct_coordinates(self):
        PLAYFIELD_MAP_2 = [[0, 0],
                           [0, 1], ]

        temp_playfield = Playfield(PLAYFIELD_MAP_2, CELL_SIZE)

        sprites = temp_playfield.walls.sprites()

        for sprite in sprites:
            self.assertEqual(sprite.rect.x, CELL_SIZE)
            self.assertEqual(sprite.rect.y, CELL_SIZE)

    def test_T_block_created_properly(self):
        self.block_generator.create_random_block()

        test_rect_group = []

        test_rect_group.append(pygame.Rect(
            4 * CELL_SIZE, 0, CELL_SIZE, CELL_SIZE))
        test_rect_group.append(pygame.Rect(
            5 * CELL_SIZE, 0, CELL_SIZE, CELL_SIZE))
        test_rect_group.append(pygame.Rect(
            5 * CELL_SIZE, 1 * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        test_rect_group.append(pygame.Rect(
            6 * CELL_SIZE, 0, CELL_SIZE, CELL_SIZE))

        indexilista = []

        for sprite in self.playfield.active_block:
            indexi = sprite.rect.collidelist(test_rect_group)
            self.assertNotEqual(indexi, -1)

    def test_block_moves_correctly(self):

        TEST_BLOCK_4 = ([["x", "x", "x", "x", 2, "x", "x", "x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]], (153, 51, 255))
        BLOCKS = [TEST_BLOCK_4]
        block_generator = BlockGenerator(self.playfield, BLOCKS)
        block_generator.create_random_block()

        test_sprite = self.create_sprite(4 * CELL_SIZE, 1, CELL_SIZE)

        self.playfield.move_group(self.playfield.active_block, 0, CELL_SIZE)

        for sprite123 in self.playfield.active_block:
            self.assertEqual(pygame.sprite.collide_rect(
                sprite123, test_sprite), True)
            #self.assertNotEqual(indexi, -1)

    def test_block_cant_move_through_wall(self):
        PLAYFIELD_MAP_3 = [[0],
                           [1]]
        TEST_BLOCK_1 = ([[2]], (50, 50, 50))
        BLOCKS = [TEST_BLOCK_1]

        temp_playfield = Playfield(PLAYFIELD_MAP_3, CELL_SIZE)

        block_generator = BlockGenerator(temp_playfield, BLOCKS)
        block_generator.create_random_block()

        test_sprite = self.create_sprite(0, 0, CELL_SIZE)

        temp_playfield.move_group(temp_playfield.active_block, 0, CELL_SIZE)
        temp_playfield.move_group(temp_playfield.active_block, 0, CELL_SIZE)

        for sprite in self.playfield.active_block:
            self.assertEqual(pygame.sprite.collide_rect(
                sprite123, test_sprite), True)

    def test_lock_block(self):
        self.block_generator.create_random_block()

        self.playfield.move_active_block_to_locked()

        self.assertEqual(len(self.playfield.active_block), 0)
        self.assertNotEqual(len(self.playfield.locked_blocks), 0)

    def test_full_lines_cleared_correctly(self):
        TEST_BLOCK = (
            [["x", 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "x"]], (153, 51, 255))
        BLOCKS = [TEST_BLOCK]
        block_generator = BlockGenerator(self.playfield, BLOCKS)
        block_generator.create_random_block()

        self.playfield.start_locking()

        self.assertEqual(len(self.playfield.locked_blocks), 0)

    def test_multiple_full_lines_cleared_correctly(self):
        TEST_BLOCK = ([["x", 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "x"],
                       ["x", 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "x"]], (153, 51, 255))
        BLOCKS = [TEST_BLOCK]
        block_generator = BlockGenerator(self.playfield, BLOCKS)
        block_generator.create_random_block()

        self.playfield.start_locking()

        self.assertEqual(len(self.playfield.locked_blocks), 0)

    def test_remaining_lines_moved_down_correctly(self):
        TEST_BLOCK = ([["x", "x", "x", "x", "x", "x", "x", 2, 2, "x", "x", "x"],
                       ["x", 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "x"]], (153, 51, 255))
        BLOCKS = [TEST_BLOCK]
        block_generator = BlockGenerator(self.playfield, BLOCKS)
        block_generator.create_random_block()

        self.playfield.start_locking()

        for sprite123 in self.playfield.locked_blocks:
            self.assertEqual(sprite123.rect.y, CELL_SIZE)

    def test_rotation(self):
        TEST_BLOCK = ([["x", "x", "x", "x", "x", 2, 2, "x",
                      "x", "x", "x", "x"]], (153, 51, 255))
        BLOCKS = [TEST_BLOCK]
        block_generator = BlockGenerator(self.playfield, BLOCKS)
        block_generator.create_random_block()

        lista = []

        self.playfield.rotate_active_block(90)
        for block_sprite in self.playfield.active_block:
            print(block_sprite.offset_vector)
            print(block_sprite.rect.x)
            print(block_sprite.rect.y)
            if block_sprite.rect.y == 1 * self.playfield.cell_size:
                lista.append(block_sprite)
        self.assertEqual(len(lista), 1)
