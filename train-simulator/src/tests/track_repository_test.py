
import unittest
from entities.track import Track
from repositories.track_repository import TrackRepository
from database_connection import get_database_connection


class TestTrack(unittest.TestCase):
    def setUp(self):
        connection = get_database_connection()
        self.track_repository = TrackRepository(connection)

    def test_station_xy_coordinates(self):
        self.assertEqual(self.track_repository.station_xy_coordinates("Hämeenlinna-P"), (100, 298))

    def test_stop_type_station(self):
        self.assertEqual(self.track_repository.stop_type("Hämeenlinna-P"), "station")

    def test_stop_type_bottleneck(self):
        self.assertEqual(self.track_repository.stop_type("Kapeikko1-P"), "bottleneck")

    def test_return_all_bottlenecks(self):
        self.assertEqual(self.track_repository.return_all_bottlenecks(), ['Kapeikko1-P', 'Kapeikko1-E'])

    def test_distance_to_next_stop(self):
        self.assertEqual(self.track_repository.distance_to_next_stop("Hämeenlinna-P"), 90)

    def test_next_stop(self):
        self.assertEqual(self.track_repository.next_stop("Hämeenlinna-P"), "Tampere-P")

    def test_speedlimit_to_next_stop(self):
        self.assertEqual(self.track_repository.speedlimit_to_next_stop("Hämeenlinna-P"), 120)