import pygame


class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()
        self.lock_counter = 0

    def tick(self, fps):
        self._clock.tick(fps)
