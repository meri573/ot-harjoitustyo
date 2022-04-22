import pygame


class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()
        self.frame_counter = 0
        self.lock_counter = 0
        self.gravity_counter = 0
        self.last_pressed_key_frame = 0
        self.last_autorepeat = 0

    def tick_tock(self, fps):
        self._clock.tick(fps)
        self.frame_counter += 1

    def gravity_tick(self, gravity):
        self.gravity_counter += gravity

    def lock_counter_tick(self):
        self.lock_counter += 1

    def lock_counter_reset(self):
        self.lock_counter = 0

    def set_last_pressed_key_frame(self):
        self.last_pressed_key_frame = self.frame_counter

    def set_last_autorepeat(self):
        self.last_autorepeat = self.frame_counter