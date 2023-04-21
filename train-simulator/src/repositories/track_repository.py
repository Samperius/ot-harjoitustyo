class TrackRepository:
    def __init__(self, connection):
        self._connection = connection
    def station_xy_coordinates(self):
        return ((0, 25))

    def distance_to_next_stop(self, dest):
        cursor = self._connection.cursor()
        cursor.execute(f"select distance from track where dest='{dest}'")
        element = cursor.fetchone()[0]
        return element

    def next_stop(self, start):
        cursor = self._connection.cursor()
        print(start)
        cursor.execute(f"select dest from track where start='{start}'")
        try:
            element = cursor.fetchone()[0]
        except:
            return

        print(element)
        return element

    def speedlimit_to_next_stop(self, dest):
        cursor = self._connection.cursor()
        cursor.execute(f"select speedlimit from track where dest='{dest}'")
        element = cursor.fetchone()[0]
        return element