import pygame
from playfield import Playfield

CELL_SIZE = 50

PLAYFIELD_MAP = [[1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1]]




def main():
    height = len(PLAYFIELD_MAP)
    width = len(PLAYFIELD_MAP[0])
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))

    level = Playfield(PLAYFIELD_MAP, CELL_SIZE)
    
    pygame.init()

    level.all_sprites.draw(display)

    #pygame.display.update()








if __name__=="__main__":
    main()