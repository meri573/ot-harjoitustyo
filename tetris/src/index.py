import pygame
from playfield import Playfield
from clock import Clock
from game_loop import GameLoop
from block_generator import BlockGenerator

CELL_SIZE = 45

PLAYFIELD_MAP = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

TEST_BLOCK_T = ([["x", "x", "x", "x", 2, 2, 2, "x", "x", "x", "x", "x"],
                ["x", "x", "x", "x", "x", 2, "x", "x", "x", "x", "x", "x"]], (153, 51, 255))

GRAVITY_LIST = [60]

# TEST_BLOCK_1 =  ([["x", "x", "x", "x", 2, "x", "x", "x", "x", "x", "x", "x"],
# ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]], (153, 51, 255))

BLOCKS = [TEST_BLOCK_T]


def main():

    pygame.init()

    height = len(PLAYFIELD_MAP)
    width = len(PLAYFIELD_MAP[0])
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))

    clock = Clock()

    playfield = Playfield(PLAYFIELD_MAP, CELL_SIZE)

    playfield.all_sprites.draw(display)



    block_generator = BlockGenerator(playfield, BLOCKS)

    game_loop = GameLoop(CELL_SIZE, playfield, block_generator, display, clock)

    game_loop.start()


if __name__ == "__main__":
    main()
