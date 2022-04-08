import pygame


class GameLoop:
    def __init__(self, cell_size, level, block_generator, display, clock):
        self._cell_size = cell_size
        self._level = level
        self._block_generator = block_generator
        self._display = display
        self._clock = clock

    def start(self):

        running = True

        while running:

            self._level.all_sprites.draw(self._display)
            pygame.display.update()

            self._clock.tick(60)
