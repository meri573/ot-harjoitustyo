import math


class Points:
    """Pisteistä huolehtiva luokka.
    """

    def __init__(self):
        self.score = 0
        self.level = 0

    def add_score(self, lines_cleared, level):
        """Lisää halutun määrän pisteitä pistelaskuriin

        Args:
            lines_cleared: Kuinka monta linjaa poistettiin kerralla.
            level: tämänhetkinen level
        """
        self.score += int(math.ceil(((level + lines_cleared)/4)*lines_cleared))

    def raise_level(self, amount=1):
        self.level += amount
