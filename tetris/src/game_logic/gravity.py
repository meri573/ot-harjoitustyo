class Gravity:
    """Palikan painovoimasta huolehtiva luokka.
    """

    def __init__(self, gravity_list, level_set):
        self._gravity_list = gravity_list
        self._level_set = level_set
        self.gravity_step = None
        self._i = 0

    def _next_gravity(self):
        """Valitsee painovoimalistasta seuraavan painovoiman ja asettaa gravity_step:n siksi.
        """
        if self._i < len(self._gravity_list):
            self.gravity_step = self._gravity_list[self._i]
            self._i += 1

    def check_level(self, level):
        """Tarkistaa onko tämänhetkisellä levelillä tarkoitus nostaa painovoimaa.

        Args:
            level: tämänhetkinen level
        """
        if level in self._level_set:
            self._next_gravity()
