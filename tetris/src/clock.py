import pygame

class Clock:
    def __init__(self, playfield):
        self._clock = pygame.time.Clock()
        self._lock_counter = 0
        self._playfield = playfield

    def tick(self, fps):
        self._clock.tick(fps)
        if self._playfield.can_move_down():
            self._lock_counter += 1
            if self._lock_counter >30:
                self.playfield.move_active_block_to_inactive()
        else:
            self._lock_counter = 0
