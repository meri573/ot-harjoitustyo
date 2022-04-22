import pygame


class GameLoop:
    def __init__(self, cell_size, playfield, block_generator, renderer, clock, gravity, points):
        self._cell_size = cell_size
        self._playfield = playfield
        self._block_generator = block_generator
        self._renderer = renderer
        self._clock = clock
        self._gravity = gravity
        self._points = points

        self._last_pressed_key = None
        
        self._level = 0

    def start(self):

        running = True

        self._block_generator.create_random_block()
        self._gravity.check_level(self._level)

        while running:

            self._event_handling()

            self._gravity_check()

            self._block_locking_check()
            if self._playfield.check_if_active_block_inside_locked_block():
                print(f"you gained {self._points.points} points")
                print(f"you reached level {self._level}")
                break

            self._renderer.render()

            self._clock.gravity_tick(self._gravity.gravity_step)
            self._clock.tick_tock(60)

    def _event_handling(self):

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

    #def _set_last_pressed_key_and_tick(self, key):
        #self._last_pressed_key = key
        #self._clock.set_last_pressed_key_frame()

    def _autorepeat(self, key, keys):
        if keys[key] and self._clock.frame_counter - self._clock.last_pressed_key_frame > 15:
            return self._clock.frame_counter - self._clock.last_autorepeat > 2

    def _block_locking_check(self):
        if not self._playfield.can_move_down():
            self._clock.lock_counter_tick()
            if self._clock.lock_counter > 30:
                # janky code alert
                # self._playfield.start_locking() also returns amount of lines cleared
                # they are then added to self._level
                cleared_line_count = self._playfield.start_locking()
                if bool(cleared_line_count):
                    self._points.add_points(cleared_line_count, self._level)
                for i in range(cleared_line_count):
                    self._level += 1
                    self._gravity.check_level(self._level)
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
        self._block_generator.create_random_block()
        if self._level % 100 != 99:
            self._level += 1
            self._gravity.check_level(self._level)
