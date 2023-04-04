import unittest
from src.entities.track import Track

class TestTrack(unittest.TestCase):
    def setUp(self):
        # Dummy data to the first test's development. later stops etc. are imported from a database
        stops = ["Helsinki", "Pasila", "Tikkurila", "Hämeenlinna",
                 "Tampere"]  # this data should be imported from database - to be modified later
        speed_limit = {"Pasila": 60, "Tikkurila": 70, "Hämeenlinna": 120,
                       "Tampere": 100}  # this data should be imported from database - to be modified later
        distances = {"Pasila": 5, "Tikkurila": 15, "Hämeenlinna": 100,
                     "Tampere": 100}  # this data should be imported from database - to be modified later

        self.track = Track("Helsinki", "Tampere", stops, speed_limit, distances)

    def test_track_names(self):
        self.assertEqual(self.track.name, "Helsinki-Tampere")

    def test_next_stop_beginning(self):
       self.assertEqual(self.track.next_stop("Helsinki"), "Pasila")

    def test_next_stop_for_last_stop(self):
        self.assertEqual(self.track.next_stop("Tampere"), "Tampere")
