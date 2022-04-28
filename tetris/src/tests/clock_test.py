import unittest

from game_logic.clock import Clock

class TestClock(unittest.TestCase):
    def setUp(self):
        self.clock = Clock()

    def test_frame_counter(self):
        self.clock.tick_tock(0)
        self.assertEqual(self.clock.frame_counter, 1)

    def test_gravity_tick(self):
        self.clock.gravity_tick(64)
        self.assertEqual(self.clock.gravity_counter, 64)

    def test_lock_counter_tick(self):
        self.clock.lock_counter_tick()
        self.assertEqual(self.clock.lock_counter, 1)

    def test_lock_counter_reset(self):
        self.clock.lock_counter_tick()
        self.clock.lock_counter_reset()
        self.assertEqual(self.clock.lock_counter, 0)

    def test_set_last_pressed_key_frame(self):
        self.clock.tick_tock(0)
        self.clock.set_last_pressed_key_frame()
        self.assertEqual(self.clock.last_pressed_key_frame, 1)

    def test_set_last_autorepeat(self):
        self.clock.tick_tock(0)
        self.clock.set_last_autorepeat()
        self.assertEqual(self.clock.last_autorepeat , 1)