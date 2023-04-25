class TrackRepository:
    def __init__(self, connection):
        self._connection = connection

    def station_xy_coordinates(self, stop):
        cursor = self._connection.cursor()
        cursor.execute(f"select x from stop_coordinates where stop='{stop}'")
        x = cursor.fetchone()[0]
        cursor.execute(f"select y from stop_coordinates where stop='{stop}'")
        y = cursor.fetchone()[0]
        return (x,y)

    def bottleneck_xy_coordinates(self, bottleneck):
        cursor = self._connection.cursor()
        cursor.execute(f"select x from bottlenecks where bottleneck='{bottleneck}'")
        x = cursor.fetchone()[0]
        cursor.execute(f"select y from bottlenecks where bottleneck='{bottleneck}'")
        y = cursor.fetchone()[0]
        return (x,y)

    def return_all_start_stops(self):
        cursor = self._connection.cursor()
        cursor.execute(f"select start from track")
        start = cursor.fetchall()
        stops = []
        for stop in start:
            stops.append(stop[0])
        return stops

    def return_all_bottlenecks(self):
        cursor = self._connection.cursor()
        cursor.execute(f"select bottleneck from bottlenecks")
        bottlenecks = cursor.fetchall()
        bottlenecks_list = []
        for bottleneck in bottlenecks:
            bottlenecks_list.append(bottleneck[0])
        return bottlenecks_list

    def distance_to_next_stop(self, dest):
        cursor = self._connection.cursor()
        cursor.execute(f"select distance from track where dest='{dest}'")
        element = cursor.fetchone()[0]
        return element

    def next_stop(self, start):
        cursor = self._connection.cursor()
        cursor.execute(f"select dest from track where start='{start}'")
        try:
            element = cursor.fetchone()[0]
        except TypeError:
            return
        return element

    def speedlimit_to_next_stop(self, dest):
        cursor = self._connection.cursor()
        cursor.execute(f"select speedlimit from track where dest='{dest}'")
        element = cursor.fetchone()[0]
        return element