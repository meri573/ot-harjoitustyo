import unittest
from playfield import Playfield


PLAYFIELD_MAP = [[0, 0],
                 [0, 1], ]
CELL_SIZE = 50


class TestPlayfield(unittest.TestCase):
    def setUp(self):
        self.playfield = Playfield(PLAYFIELD_MAP, CELL_SIZE)

    def test_wall_created_in_correct_coordinates(self):

        sprites = self.playfield.walls.sprites()

        for sprite in sprites:
            self.assertEqual(sprite.rect.x, CELL_SIZE)
            self.assertEqual(sprite.rect.y, CELL_SIZE)
