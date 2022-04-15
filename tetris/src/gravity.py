import pygame


class Gravity:
    def __init__(self, gravity_list):
        self._gravity_list = gravity_list
        self.gravity_step = None
        self._i = 0

    def next_gravity(self):
        if self._i < len(self._gravity_list):
            self.gravity_step = self._gravity_list[self._i]
            self._i += 1
