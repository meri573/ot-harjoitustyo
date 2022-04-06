import pygame

class GameLoop:
    def __init__(self, cell_size, level, block_generator):
        self._cell_size = cell_size
        self._level = level
        self._block_generator = block_generator


    def start(self):

        running = True

        while running:

            level.all_sprites.draw(display)
            pygame.display.update()

            clock.tick(60)