import pygame
import unittest
from playfield import Playfield
from block_generator import BlockGenerator

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


CELL_SIZE = 50


class TestPlayfield(unittest.TestCase):
    def setUp(self):
        self.playfield = Playfield(PLAYFIELD_MAP, CELL_SIZE)
        

    def test_wall_created_in_correct_coordinates(self):
        PLAYFIELD_MAP_2 = [[0, 0],
                        [0, 1], ]
        
        temp_playfield = Playfield(PLAYFIELD_MAP_2, CELL_SIZE)
            
        sprites = temp_playfield.walls.sprites()

        for sprite in sprites:
            self.assertEqual(sprite.rect.x, CELL_SIZE)
            self.assertEqual(sprite.rect.y, CELL_SIZE)

    def test_T_block_created_properly(self):
        
        TEST_BLOCK_T = ([["x", "x", "x", "x", 2, 2, 2, "x", "x", "x", "x", "x"],
                        ["x", "x", "x", "x", "x", 2, "x", "x", "x", "x", "x", "x"]], (153, 51, 255))

        BLOCKS = [TEST_BLOCK_T]

        block_generator = BlockGenerator(self.playfield, BLOCKS)
        block_generator.create_random_block()
        
        test_rect_group = []

        test_rect_group.append(pygame.Rect(4 * CELL_SIZE, 0, CELL_SIZE, CELL_SIZE))
        test_rect_group.append(pygame.Rect(5 * CELL_SIZE, 0, CELL_SIZE, CELL_SIZE))
        test_rect_group.append(pygame.Rect(5 * CELL_SIZE, 1 * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        test_rect_group.append(pygame.Rect(6 * CELL_SIZE, 0, CELL_SIZE, CELL_SIZE))

        indexilista = []

        for sprite in self.playfield.active_block:
            indexi = sprite.rect.collidelist(test_rect_group)
            self.assertNotEqual(indexi, -1)

