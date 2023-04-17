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

    level = Level(LEVEL_MAP, CELL_SIZE, DEFAULT_IMAGE_SIZE, display)

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

def run_ui2(Level):
    height = LEVEL_MAP.shape[0]
    width = LEVEL_MAP.shape[1]
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE

    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Train simulator")

    level = Level(LEVEL_MAP, CELL_SIZE, DEFAULT_IMAGE_SIZE, display)

    event_queue = EventQueue()
    renderer = Renderer(display, level)
    clock = Clock()
    game_loop = GameLoop(level, renderer, event_queue, clock, CELL_SIZE)

    pygame.init()
    game_loop.start(simulate, level, Track, Train, DEFAULT_IMAGE_SIZE)


class GameLoop:
    def __init__(self, level, renderer, event_queue, clock, cell_size):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size

    def start(self, simulate, level, Track, Train, DEFAULT_IMAGE_SIZE):
        simulate(level, Track, Train, 5, DEFAULT_IMAGE_SIZE)
        while True:
            if self._handle_events() == False:
                break

            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._level.move_robot(dx=-self._cell_size)
                if event.key == pygame.K_RIGHT:
                    self._level.move_robot(dx=self._cell_size)
                if event.key == pygame.K_UP:
                    self._level.move_robot(dy=-self._cell_size)
                if event.key == pygame.K_DOWN:
                    self._level.move_robot(dy=self._cell_size)
            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()

class EventQueue:
    def get(self):
        return pygame.event.get()

class Renderer:
    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render(self):
        self._level.all_sprites.draw(self._display)

        pygame.display.update()

class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        self._clock.tick(fps)

    def get_ticks(self):
        return pygame.time.get_ticks()


if __name__ == "__main__":
    run_ui()