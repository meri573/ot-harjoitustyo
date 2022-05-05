import pygame

from score_database.score_repository import score_repository


class GameLoop:
    """Pelisilmukasta vastaava luokka.
    """

    def __init__(self, playfield, block_generator, renderer, clock, gravity, points):
        self._cell_size = playfield.cell_size
        self._playfield = playfield
        self._block_generator = block_generator
        self._renderer = renderer
        self._clock = clock
        self._gravity = gravity
        self._points = points

    def start(self):

        running = True

        self._block_generator.create_block()
        self._block_generator.create_block()
        self._gravity.check_level(self._points.level)

        while running:

            self._event_handling()

            self._gravity_check()

            self._block_locking_check()
            if self._playfield.check_if_active_block_inside_locked_block():

                break

            self._renderer.render()

            self._clock.gravity_tick(self._gravity.gravity_step)
            self._clock.tick_tock(60)

        self.score_screen()

    def score_screen(self):
        scores = score_repository.find_scores_desc()

        name = ["_", "_", "_"]
        i = 0

        inputting = True

        self._renderer.render_scoreboard(scores)

        while inputting:
            char = self._handle_keydowns_score_screen()

            if char == pygame.K_RETURN:
                score_repository.save_score("".join(name), self._points.score)
                inputting = False

            elif char == pygame.K_BACKSPACE:
                name[i] = "_"
                if i > 0:
                    i -= 1

            elif isinstance(char, str):
                name[i] = char

                if i < 2:
                    i += 1

            self._renderer.render_name_submission(name)
            self._clock.tick_tock(60)

    def _handle_keydowns_score_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return pygame.K_BACKSPACE

                if event.key == pygame.K_RETURN:
                    return pygame.K_RETURN

                if event.unicode.isalpha():
                    return event.unicode
        return None

    def _event_handling(self):
        """Hoitaa näppäinten painallukset.
        """
        self._handle_keydowns()
        self._handle_pressed_keys()

    def _handle_keydowns(self):
        """Liikuttaa palikkaa halutulla tavalla tiettyjä näppäimiä painaessa.
        Viimeksi painettu nappi pistetään talteen.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._playfield.move_group(
                        self._playfield.active_block, -self._cell_size, 0)
                    self._clock.set_last_pressed_key_frame()
                if event.key == pygame.K_RIGHT:
                    self._playfield.move_group(
                        self._playfield.active_block, self._cell_size, 0)
                    self._clock.set_last_pressed_key_frame()
                if event.key == pygame.K_DOWN:
                    self._playfield.move_group(
                        self._playfield.active_block, 0, self._cell_size)
                    self._clock.set_last_pressed_key_frame()

                if event.key == pygame.K_s:
                    self._playfield.rotate_active_block(-90)
                if event.key == pygame.K_d:
                    self._playfield.rotate_active_block(90)

    def _handle_pressed_keys(self):
        """Jos näppäintä on pidetty pohjassa tarpeeksi pitkään sen aktivoima liike toistetaan.
        """
        keys = pygame.key.get_pressed()
        if self._autorepeat(pygame.K_LEFT, keys):
            self._playfield.move_group(
                self._playfield.active_block, -self._cell_size, 0)

        if self._autorepeat(pygame.K_RIGHT, keys):
            self._playfield.move_group(
                self._playfield.active_block, self._cell_size, 0)

        if self._autorepeat(pygame.K_DOWN, keys):
            self._playfield.move_group(
                self._playfield.active_block, 0, self._cell_size)

    # def _set_last_pressed_key_and_tick(self, key):
        #self._last_pressed_key = key
        # self._clock.set_last_pressed_key_frame()

    def _autorepeat(self, key, keys):
        """Tarkistaa onko viimeistä liikenappia pidetty pohjassa tarpeeksi kauan, että liike
        toistettaisiin.

        Ensin tarkistetaan, että viimeksi painettu näppäin on yhä painettu pohjaan ja sitä on
        painettu tarpeeksi pitkään pohjaan. Tämän jälkeen tarkistetaan onko viimeisestä toistetusta
        liikkeestä kulunut tarpeeksi kauan että liike voitaisiin toistaa uudelleen.

        Args:
            key: Näppäin jonka haluamme tarkistaa onko se tällä hetkellä pohjaan painettu.
            keys: Kaikki tällä hetkellä pohjaan painetut näppäimet.

        Returns:
            Palauttaa Booleanin joka kertoo täyttyykö kaikki vaaditut ehdot.
        """
        if keys[key] and self._clock.frame_counter - self._clock.last_pressed_key_frame > 15:
            return self._clock.frame_counter - self._clock.last_autorepeat > 2
        return False

    def _block_locking_check(self):
        if not self._playfield.can_move_down():
            self._clock.lock_counter_tick()
            if self._clock.lock_counter > 30:
                # janky code alert
                # self._playfield.start_locking() also returns amount of lines cleared
                # they are then added to self._level
                cleared_line_count = self._playfield.start_locking()
                if bool(cleared_line_count):
                    self._points.add_score(
                        cleared_line_count, self._points.level)
                for i in range(cleared_line_count):
                    self._points.level += 1
                    self._gravity.check_level(self._points.level)
                self._block_creation_procedure()
        else:
            self._clock.lock_counter_reset()

    def _gravity_check(self):
        if self._clock.gravity_counter >= 256:
            while self._clock.gravity_counter >= 256:
                self._playfield.move_group(
                    self._playfield.active_block, 0, self._cell_size)
                self._clock.gravity_counter -= 256

    def _block_creation_procedure(self):
        self._block_generator.create_block()
        if self._points.level % 100 != 99:
            self._points.level += 1
            self._gravity.check_level(self._points.level)
