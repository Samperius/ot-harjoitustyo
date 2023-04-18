import pygame
import numpy as np
from entities.track import Track
from entities.train import Train
from simulator.simulate import simulate

width = 200
height = 50

LEVEL_MAP = np.zeros((height,width))
LEVEL_MAP[height//2,:] = np.ones(width)
LEVEL_MAP[height//2,0] = 2
LEVEL_MAP[height//2,width-1] = 2
LEVEL_MAP[height//2,width//2] = 2
LEVEL_MAP[height//2,width//3] = 3

CELL_SIZE = 10
def run_ui(Level):
    height = LEVEL_MAP.shape[0]
    width = LEVEL_MAP.shape[1]
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE

    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Train simulator")

    level = Level(LEVEL_MAP, CELL_SIZE, display)

    pygame.init()
    level.all_sprites.draw(display)
    pygame.display.update()
    simulate(level, Track, Train, 5)
    level.all_sprites.draw(display)


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    run_ui()