import pygame

class Gravity:
    def __init__(self, gravity_list):
        self._gravity_list = gravity_list
        self.gravity = 0
        self._i = -1

    def next_gravity(self):
        self._i += 1
        if self._i < len(self._gravity_list):
            self.gravity = self._gravity_list[self._i]

