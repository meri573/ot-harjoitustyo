import pygame

class GameLoop:
    def __init__(self, cell_size, level):
        self._cell_size = cell_size
        self._level = level


    def start(self):

        running = True

        while running:

            level.all_sprites.draw(display)
            pygame.display.update()

            clock.tick(60)