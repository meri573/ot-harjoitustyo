import pygame


class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()
        self.lock_counter = 0

    def tick_tock(self, fps):
        self._clock.tick(fps)

    def lock_counter_tick(self):
        self.lock_counter += 1

    def lock_counter_reset(self):
        self.lock_counter = 0