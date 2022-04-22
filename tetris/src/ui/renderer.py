import pygame


class Renderer:
    def __init__(self, display, playfield, points):
        self._display = display
        self._playfield = playfield
        self._points = points
        self._font = pygame.font.SysFont(None, 50)

    def render(self):
        self._display.fill((150, 150, 150))
        self._playfield.all_sprites.draw(self._display)
        text1 = self._font.render(
            f"points: {self._points.points}", True, (240, 240, 240))
        text2 = self._font.render(
            f"level: {self._points.level}", True, (240, 240, 240))
        #self._display.get_width() - 5 * self._playfield.cell_size
        #self._display.get_height() - 1 * self._playfield.cell_size

        self._display.blit(text1,  (self._display.get_width(
        ) - 5 * self._playfield.cell_size, self._display.get_height() - 2 * self._playfield.cell_size))
        self._display.blit(text2, (self._display.get_width(
        ) - 5 * self._playfield.cell_size, self._display.get_height() - 1 * self._playfield.cell_size))
        pygame.display.flip()
