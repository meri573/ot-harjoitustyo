import random


class BlockGenerator:
    def __init__(self, playfield, blocks):
        self._playfield = playfield
        self._blocks = blocks

        # delta from block spawn point to next block area
        self.delta_x = 9 * self._playfield.cell_size
        self.delta_y = 1 * self._playfield.cell_size

    def create_block(self):
        self._move_to_spawnpoint()
        self._move_from_next_block_to_active()
        self.create_random_block()
        self._move_to_next_block_area()

    def create_random_block(self):

        block = random.choice(self._blocks)
        self._playfield.initialize_sprites(block[0], block[1])

    def _move_to_next_block_area(self):
        self._playfield.move_group(
            self._playfield.next_block, self.delta_x, self.delta_y)

    def _move_to_spawnpoint(self):
        # moving block without collision checks
        for block_sprite in self._playfield.next_block:
            self._playfield.move_block(
                block_sprite, -self.delta_x, -self.delta_y)

    def _move_from_next_block_to_active(self):
        self._playfield.active_block.add(self._playfield.next_block)
        self._playfield.next_block.empty()
