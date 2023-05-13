import unittest
from entities.track import Track
from repositories.track_repository import TrackRepository
from database_connection import get_database_connection


class TestTrack(unittest.TestCase):
    def setUp(self):
        connection = get_database_connection()
        track_repository = TrackRepository(connection)

        self.track = Track("Helsinki-P", "Tampere-P", track_repository)

    def test_speed_to_stop(self):
        self.assertEqual(self.track.speed_to_stop("Hämeenlinna-P"), 120)

    def test_distance_to_stop(self):
        self.assertEqual(self.track.distance_to_stop("Hämeenlinna-P"), 90)

    def test_next_stop_beginning(self):
        self.assertEqual(self.track.next_stop("Helsinki-P"), "Pasila-P")

    def test_next_stop_mid(self):
        self.assertEqual(self.track.next_stop("Tikkurila-P"), "Hämeenlinna-P")

    def test_next_stop_for_last_stop(self):
        self.assertEqual(self.track.next_stop("Jyväskylä-P"), None)

