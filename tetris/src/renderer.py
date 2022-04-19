import pygame

class Renderer:
    def __init__(self, display, playfield):
        self._display = display
        self._playfield = playfield

    def render(self):
        self._playfield.all_sprites.draw(self._display)
        pygame.display.update()