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

        self._score_and_level_text()

        pygame.display.update()

    def render_scoreboard(self, score_list):
        self._leaderboard(score_list)

        pygame.display.update()

    def render_name_submission(self, name):
        self._name_submission(name)

        pygame.display.update()


    def _name_submission(self, name):
        instruction = self._font.render(f"enter name", True, (50, 50, 50))
        self._display.blit(self._text_background(instruction, (150,150,150)),(self._display.get_width(
            )/4, 16 * self._playfield.cell_size))

        current_name = self._font.render(" ".join(name), True, (50,50,50))
        self._display.blit(self._text_background(current_name,(150,150,150)),(self._display.get_width(
            )/4, 18 * self._playfield.cell_size))


    def _score_and_level_text(self):
        points = self._font.render(
            f"points: {self._points.score}", True, (240, 240, 240))
        level = self._font.render(
            f"level: {self._points.level}", True, (240, 240, 240))

        self._display.blit(points,  (self._display.get_width(
        ) - 5 * self._playfield.cell_size, self._display.get_height() - 2 * self._playfield.cell_size))
        self._display.blit(level, (self._display.get_width(
        ) - 5 * self._playfield.cell_size, self._display.get_height() - 1 * self._playfield.cell_size))

    def _leaderboard(self, score_list):
        text = self._font.render(f"name  score", True, (50, 50, 50))
        self._display.blit(
            self._text_background(text, (150, 150, 150)), (self._display.get_width()/4, self._playfield.cell_size))

        i = 0
        for score in score_list:
            text2 = self._font.render(
                f"{score[0]}     {score[1]}", True, (40, 40, 40))

            self._display.blit(self._text_background(text2, (125, 125, 125)),  (self._display.get_width(
            )/4, 4 * self._playfield.cell_size + i * (self._font.get_height() + 20)))

            i += 1

    def _text_background(self, text, color):
        temp_surface = pygame.Surface(text.get_size())
        temp_surface.fill(color)
        temp_surface.blit(text, (0, 0))
        return temp_surface
