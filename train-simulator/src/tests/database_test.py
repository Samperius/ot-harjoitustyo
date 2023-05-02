import unittest
from entities.track import Track
from repositories.track_repository import TrackRepository
from database_connection import get_database_connection
from initialize_database import drop_tables, create_tables, initialize_database


class TestInitializeDatabase(unittest.TestCase):
    def setUp(self):
        self._connection = initialize_database()

    def test_check_track_db(self):
        cursor = self._connection.cursor()
        cursor.execute("select dest from track where start='Helsinki-P'")
        try:
            element = cursor.fetchone()[0]
        except TypeError:
            element = None
        self.assertEqual(element, 'Pasila-P')

    def test_check_track_db_last_stop(self):
        cursor = self._connection.cursor()
        cursor.execute("select dest from track where start='Jyväskylä-P'")
        try:
            element = cursor.fetchone()[0]
        except TypeError:
            element = None
        self.assertEqual(element, None)

    def test_check_coordinate_db(self):
        cursor = self._connection.cursor()
        cursor.execute("select type from stop_coordinates where stop='Helsinki-P'")
        try:
            element = cursor.fetchone()[0]
        except TypeError:
            element = None
        self.assertEqual(element, 'Pasila-P')

    def test_drop_tables(self):
        cursor = self._connection.cursor()
        drop_tables(self._connection)

        try:
            cursor.execute("select dest from track where start='Helsinki-P'")
            element = cursor.fetchone()[0]
        except:
            element = None
            pass
        initialize_database()
        self.assertEqual(element, None)