import unittest
from src.entities.track import Track
from src.repositories.track_repository import Track_repository

class TestTrack(unittest.TestCase):
    def setUp(self):
        track_repo = Track_repository()
        # Dummy data to the first test's development. later stops etc. are imported from a database
        stops = ["Helsinki", "Pasila", "Tikkurila", "Hämeenlinna",
                 "Tampere"]  # this data should be imported from database - to be modified later
        speed_limit = {"Pasila": 60, "Tikkurila": 70, "Hämeenlinna": 120,
                       "Tampere": 100}  # this data should be imported from database - to be modified later
        distances = {"Pasila": 5, "Tikkurila": 15, "Hämeenlinna": 100,
                     "Tampere": 100}  # this data should be imported from database - to be modified later

        self.track = Track("Helsinki", "Tampere", stops,
                           speed_limit, distances, track_repo)

    def test_track_names(self):
        self.assertEqual(self.track.name, "Helsinki-Tampere")

    def test_speed_to_stop(self):
        self.assertEqual(self.track.speed_to_stop("Hämeenlinna"), 120)

    def test_distance_to_stop(self):
        self.assertEqual(self.track.distance_to_stop("Hämeenlinna"), 100)

    def test_next_stop_beginning(self):
        self.assertEqual(self.track.next_stop("Helsinki"), "Pasila")

    def test_next_stop_for_last_stop(self):
        self.assertEqual(self.track.next_stop("Tampere"), "Tampere")
