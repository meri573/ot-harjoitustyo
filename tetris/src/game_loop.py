import pygame


class GameLoop:
    def __init__(self, cell_size, playfield, block_generator, display, clock):
        self._cell_size = cell_size
        self._playfield = playfield
        self._block_generator = block_generator
        self._display = display
        self._clock = clock

    def start(self):

        running = True

        self._block_generator.create_random_block()

        while running:

            self._event_handling()

            self._block_locking_check()

            self._playfield.all_sprites.draw(self._display)

            pygame.display.update()

            self._clock.tick_tock(60)

    def _event_handling(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._playfield.move_group(
                        self._playfield.active_block, -self._cell_size, 0)
                if event.key == pygame.K_RIGHT:
                    self._playfield.move_group(
                        self._playfield.active_block, self._cell_size, 0)
                if event.key == pygame.K_DOWN:
                    self._playfield.move_group(
                        self._playfield.active_block, 0, self._cell_size)

                # keys = pygame.key.get_pressed()
                # if keys[K_LEFT]:

                # if keys[K_RIGHT]:

                # if keys[K_DOWN]:

                # if keys[K_s]:
                #     pass
                # if keys[K_d]:

    def _block_locking_check(self):
        if not self._playfield.can_move_down():
            self._clock.lock_counter_tick()
            if self._clock.lock_counter > 30:
                self._playfield.move_active_block_to_locked()
                self._block_generator.create_random_block()
        else:
            self._clock.lock_counter_reset()

    def _gravity_check(self):
        pass
