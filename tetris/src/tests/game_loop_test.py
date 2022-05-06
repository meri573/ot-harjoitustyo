import unittest
import pygame

from game_logic.game_loop import GameLoop

pygame.init()


class StubPlayfield:
    def __init__(self):
        self.cell_size = 1
        self.x = 0
        self.y = 0

        self.active_block = "active_block"

    def move_group(self, group, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y


class StubBlockGenerator:
    def __init__(self):
        self.counter = 0

    def create_block(self):
        self.counter += 1


class StubRenderer:
    pass


class StubClock:
    def __init__(self):
        self.gravity_counter = 0
        self.last_pressed_key_frame = 0
        self.last_autorepeat = 0
        self.frame_counter = 0


class StubGravity:
    def __init__(self):
        self.counter = None

    def check_level(self, level):
        self.counter = level


class StubPoints:
    def __init__(self):
        self.level = 0


class TestGameLoop(unittest.TestCase):
    def setUp(self):

        self.game_loop = GameLoop(StubPlayfield(), StubBlockGenerator(
        ), StubRenderer(), StubClock(), StubGravity(), StubPoints())

    def test_gravity_check(self):
        self.game_loop._clock.gravity_counter = 0
        self.game_loop._gravity_check()
        self.assertEqual(self.game_loop._clock.gravity_counter, 0)
        self.assertEqual(self.game_loop._playfield.x, 0)
        self.assertEqual(self.game_loop._playfield.y, 0)

        self.game_loop._clock.gravity_counter = 256

        self.game_loop._gravity_check()
        self.assertEqual(self.game_loop._clock.gravity_counter, 0)
        self.assertEqual(self.game_loop._playfield.x, 0)
        self.assertEqual(self.game_loop._playfield.y, 1)

    def test_block_creation_procedure(self):

        self.game_loop._block_creation_procedure()
        self.assertEqual(self.game_loop._block_generator.counter, 1)
        self.assertEqual(self.game_loop._points.level, 1)
        self.assertEqual(self.game_loop._gravity.counter, 1)

        self.game_loop._points.level = 99
        self.game_loop._block_creation_procedure()
        self.assertEqual(self.game_loop._block_generator.counter, 2)
        self.assertEqual(self.game_loop._points.level, 99)
        self.assertEqual(self.game_loop._gravity.counter, 1)

    def test_autorepeat(self):
        key = "K_DOWN"

        keys = {"K_DOWN": True}

        self.assertEqual(self.game_loop._autorepeat(key, keys), False)

        self.game_loop._clock.frame_counter = 16
        self.last_autorepeat = 3

        self.assertEqual(self.game_loop._autorepeat(key, keys), True)
