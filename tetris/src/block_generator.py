import pygame
import random



class BlockGenerator:
    def __init__(self, playfield, blocks):
        self._playfield = playfield
        self._blocks = blocks

    def create_random_block(self):
        block = random.choice(self._blocks)
        