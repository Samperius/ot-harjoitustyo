import pygame
from ui.static_sprites import StaticSprite
import numpy as np

class Ui:
    def __init__(self, MAP, CELL_SIZE, display):
        self.cell_size = CELL_SIZE
        self.trains = pygame.sprite.Group()
        self.tracks = pygame.sprite.Group()
        self.forests = pygame.sprite.Group()
        self.stops = pygame.sprite.Group()
        self.bottlenecks = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.MAP = MAP
        self._initialize_sprites(MAP)
        self.display = display

    def _initialize_sprites(self, MAP, ):
        height = MAP.shape[0]
        width = MAP.shape[1]

        for y in range(height):
            for x in range(width):
                cell = MAP[y,x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.forests.add(StaticSprite(normalized_x, normalized_y, self.cell_size, pygame.Color(0, 255, 0, 255)))
                elif cell == 1:
                    self.tracks.add(StaticSprite(normalized_x, normalized_y, self.cell_size, pygame.Color(190, 190, 190, 255)))
                elif cell == 2:
                    self.stops.add(StaticSprite(normalized_x, normalized_y, self.cell_size, pygame.Color(0, 0, 0, 255)))
                elif cell == 3:
                    self.bottlenecks.add(StaticSprite(normalized_x, normalized_y, self.cell_size, pygame.Color(255, 165, 0, 255)))

        self.all_sprites.add(
            self.forests,
            self.tracks,
            self.stops,
            self.bottlenecks,
        )

    def draw_train(self, train):
        train.rect.x = train.rect.x * self.cell_size
        train.rect.y = train.rect.y * self.cell_size
        self.trains.add(train)
        self.all_sprites.add(
            self.trains
        )
        self.all_sprites.draw(self.display)