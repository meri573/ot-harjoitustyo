import random
import pygame



class BlockGenerator:
    def __init__(self, playfield, blocks):
        self._playfield = playfield
        self._blocks = blocks

    def create_random_block(self):
        block = random.choice(self._blocks)
        self._playfield.initialize_sprites(block[0], block[1])
