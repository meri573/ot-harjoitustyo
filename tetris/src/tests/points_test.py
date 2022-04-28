import unittest

from game_logic.points import Points

class TestPoints(unittest.TestCase):
    def setUp(self):
        self.points = Points()

    def test_raise_level(self):
        self.points.raise_level(1)
        self.assertEqual(self.points.level, 1)

    def test_point_counter_rounding(self):
        #self.points.raise_level(2)
        self.points.add_score(1, 1)
        print(self.points.level)
        self.assertEqual(self.points.score, 1)
        self.points.score = 0
        self.points.add_score(3, 2)
        self.assertEqual(self.points.score, 4)