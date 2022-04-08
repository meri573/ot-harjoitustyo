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

        move_counter = 0
        gravity_counter = 0
        moved_on_last_frame = False

        self._block_generator.create_random_block()

        while running:

            self._event_handling(
                move_counter, gravity_counter, moved_on_last_frame)

            self._playfield.all_sprites.draw(self._display)
            pygame.display.update()

            self._clock.tick(60)

    def _event_handling(self, move_counter, gravity_counter, moved_on_last_frame):

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
