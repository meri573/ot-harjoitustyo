import math


class Points:
    def __init__(self):
        self.points = 0
        self.level = 0

    def add_points(self, lines_cleared, level):
        self.points += int(math.ceil((level + lines_cleared)/4)*lines_cleared)

    def raise_level(self, amount = 1):
        self.level += 1