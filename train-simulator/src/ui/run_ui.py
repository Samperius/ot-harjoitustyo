import pygame
import numpy as np
from entities.track import Track
from entities.train import Train
from simulator.simulate import simulate

width = 50
height = 5

LEVEL_MAP = np.zeros((height,width))
LEVEL_MAP[height//2,:] = np.ones(width)
LEVEL_MAP[height//2,0] = 2
LEVEL_MAP[height//2,width-1] = 2
LEVEL_MAP[height//2,width//2] = 2
LEVEL_MAP[height//2,width//3] = 3

CELL_SIZE = 50
DEFAULT_IMAGE_SIZE = np.array((CELL_SIZE, CELL_SIZE))

def run_ui(Level):
    height = LEVEL_MAP.shape[0]
    width = LEVEL_MAP.shape[1]
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE

    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Train simulator")

    level = Level(LEVEL_MAP, CELL_SIZE, DEFAULT_IMAGE_SIZE)

    pygame.init()
    level.all_sprites.draw(display)
    simulate(level, Track, Train, 5, DEFAULT_IMAGE_SIZE)
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