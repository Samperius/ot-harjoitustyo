import unittest
from src.entities.train import Train
from src.entities.track import Track
from src.repositories.track_repository import Track_repository
import simpy
from src.ui.level import Level
import numpy as np
import pygame

width = 200
height = 50

LEVEL_MAP = np.zeros((height,width))
LEVEL_MAP[height//2,:] = np.ones(width)
LEVEL_MAP[height//2,0] = 2
LEVEL_MAP[height//2,width-1] = 2
LEVEL_MAP[height//2,width//2] = 2
LEVEL_MAP[height//2,width//3] = 3

CELL_SIZE = 10
DEFAULT_IMAGE_SIZE = np.array((CELL_SIZE, CELL_SIZE))


class TestTrack(unittest.TestCase):
    def setUp(self):
        # Dummy data to the first test's development. later stops etc. are imported from a database
        stops = ["Helsinki", "Pasila", "Tikkurila", "Hämeenlinna",
                 "Tampere"]  # this data should be imported from database - to be modified later
        speed_limit = {"Pasila": 60, "Tikkurila": 70, "Hämeenlinna": 120,
                       "Tampere": 100}  # this data should be imported from database - to be modified later
        distances = {"Pasila": 5, "Tikkurila": 15, "Hämeenlinna": 100,
                     "Tampere": 100}  # this data should be imported from database - to be modified later

        display_height = height * CELL_SIZE
        display_width = width * CELL_SIZE
        display = pygame.display.set_mode((display_width, display_height))
        level = Level(LEVEL_MAP, CELL_SIZE, DEFAULT_IMAGE_SIZE, display)
        track_repo = Track_repository()

        self.track = Track("Helsinki", "Tampere", stops,
                           speed_limit, distances, track_repo)
        bottleneck = simpy.PreemptiveResource(env, capacity=1)
        self.train = Train(env, f"Train {1}","Helsinki", "Tampere", bottleneck, self.track, level)

    def test_move_x_train(self):
        before_move = self.train.rect.x
        after_move = self.train.move_train(11,0)
        self.assertEqual(before_move + 11, after_move)
