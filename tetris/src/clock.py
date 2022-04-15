import pygame


class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()
        self.lock_counter = 0
        self.gravity_counter = 0

    def tick_tock(self, fps):
        self._clock.tick(fps)

    def gravity_tick(self, gravity):
        self.gravity_counter += gravity

    def lock_counter_tick(self):
        self.lock_counter += 1

    def lock_counter_reset(self):
        self.lock_counter = 0