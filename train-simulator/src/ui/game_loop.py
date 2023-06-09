import pygame

class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        self._clock.tick(fps)

    def get_ticks(self):
        return pygame.time.get_ticks()

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

class GameLoop:
    def __init__(self, renderer, event_queue, clock, cell_size):
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size
        self.running = True

    def start(self):
        while self.running:
            if self._handle_events() == False:
                break

            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

    def _render(self):
        self._renderer.render()