import pygame
from game_logic.playfield import Playfield
from game_logic.clock import Clock
from game_logic.game_loop import GameLoop
from game_logic.block_generator import BlockGenerator
from game_logic.gravity import Gravity
from game_logic.points import Points
from ui.renderer import Renderer

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

T_BLOCK = ([["x", "x", "x", "x", 3, 3, 3, "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", 3, "x", "x", "x", "x", "x", "x"]], (0, 255, 255))

I_BLOCK = ([["x", "x", "x", "x", 3, 3, 3, 3, "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]], (229, 84, 6))

L_BLOCK = ([["x", "x", "x", "x", 3, 3, 3, "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", 3, "x", "x", "x", "x", "x", "x", "x"]], (255, 150, 50))

J_BLOCK = ([["x", "x", "x", "x", 3, 3, 3, "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", 3, "x", "x", "x", "x", "x"]], (100, 135, 247))

Z_BLOCK = ([["x", "x", "x", "x", 3, 3, "x", "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", 3, 3, "x", "x", "x", "x", "x"]], (40, 255, 120))

S_BLOCK = ([["x", "x", "x", "x", "x", 3, 3, "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", 3, 3, "x", "x", "x", "x", "x", "x"]], (255, 51, 255))

O_BLOCK = ([["x", "x", "x", "x", "x", 3, 3, "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", 3, 3, "x", "x", "x", "x", "x"]], (255, 255, 100))

# GRAVITY_LIST and LEVEL_SET could be combined into a dictionary

GRAVITY_LIST = [4, 6, 8, 10, 12, 16, 32, 48, 64, 80, 96, 112, 128, 144, 4,
                32, 64, 96, 128, 160, 192, 224, 256, 512, 768, 1024, 1280, 1024, 768, 5120]

LEVEL_SET = {0, 30, 35, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 170, 200,
             220, 230, 233, 236, 239, 243, 247, 251, 300, 330, 360, 400, 420, 450, 500}

BLOCKS = [T_BLOCK, I_BLOCK, L_BLOCK, J_BLOCK, Z_BLOCK, S_BLOCK, O_BLOCK]

PIVOT_POINT = (5.5 * CELL_SIZE, 0.5 * CELL_SIZE)


def main():

    pygame.init()

    height = len(PLAYFIELD_MAP)
    width = len(PLAYFIELD_MAP[0])
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE + 6 * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))

    clock = Clock()

    gravity = Gravity(GRAVITY_LIST, LEVEL_SET)

    playfield = Playfield(PLAYFIELD_MAP, CELL_SIZE, PIVOT_POINT)

    points = Points()

    renderer = Renderer(display, playfield, points)

    playfield.all_sprites.draw(display)

    block_generator = BlockGenerator(playfield, BLOCKS)

    game_loop = GameLoop(playfield,
                         block_generator, renderer, clock, gravity, points)

    game_loop.start()


if __name__ == "__main__":
    main()
