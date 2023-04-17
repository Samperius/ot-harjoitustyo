import pygame
from ui.static_sprites import Forest
from ui.static_sprites import Track
from ui.static_sprites import Stop
from ui.static_sprites import Bottleneck

import numpy as np

class Level:
    def __init__(self, level_map, cell_size, DEFAULT_IMAGE_SIZE, display):
        self.cell_size = cell_size
        self.trains = pygame.sprite.Group()
        self.tracks = pygame.sprite.Group()
        self.forests = pygame.sprite.Group()
        self.stops = pygame.sprite.Group()
        self.bottlenecks = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.default_image_size = DEFAULT_IMAGE_SIZE
        self.level_map = level_map
        self._initialize_sprites(level_map, DEFAULT_IMAGE_SIZE)
        self.display = display

    def _initialize_sprites(self, level_map, DEFAULT_IMAGE_SIZE):
        height = level_map.shape[0]
        width = level_map.shape[1]

        for y in range(height):
            for x in range(width):
                cell = level_map[y,x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.forests.add(Forest(normalized_x, normalized_y, DEFAULT_IMAGE_SIZE))
                elif cell == 1:
                    self.tracks.add(Track(normalized_x, normalized_y, DEFAULT_IMAGE_SIZE))
                elif cell == 2:
                    self.stops.add(Stop(normalized_x, normalized_y, DEFAULT_IMAGE_SIZE))
                elif cell == 3:
                    self.bottlenecks.add(Bottleneck(normalized_x, normalized_y, DEFAULT_IMAGE_SIZE))

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
        print("olen täällä")
        self.all_sprites.add(
            self.trains
        )
        self.all_sprites.draw(self.display)




    def update_train(self):
        #tässä päivitetään junien sijainnit?
        ...