import unittest
import pygame

from game_logic.gravity import Gravity

GRAVITY_LIST = [4, 50]
LEVEL_SET = {0, 30}


class TestGravity(unittest.TestCase):
    def setUp(self):
        self.gravity = Gravity(GRAVITY_LIST, LEVEL_SET)

    def test_gravity_changes_correctly(self):
        self.gravity.check_level(0)
        self.assertEqual(self.gravity.gravity_step, 4)
        self.gravity.check_level(30)
        self.assertEqual(self.gravity.gravity_step, 50)
        self.gravity.check_level(50)
        self.assertEqual(self.gravity.gravity_step, 50)

    def test_gravity_list_index_doesnt_got_out_of_bounds(self):
        self.gravity.check_level(0)
        self.gravity.check_level(30)
        self.gravity.check_level(30)
        self.assertEqual(self.gravity.gravity_step, 50)
