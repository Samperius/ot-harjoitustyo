class TrackRepository:
    """
    Tietokantaluokka, joka hakee radan tiedot SQlite tietokannasta

    attributes:
        _connection: sqlite3.connect-muuttuja
    """
    def __init__(self, connection):
        """
        Luokan konstruktori
        :param connection: sqlite3.connect-muuttuja
        """
        self._connection = connection

    def station_xy_coordinates(self, stop):
        """
        metodi palauttaa aseman koordinaatin
        :param stop: merkkijono, joka kertoo aseman
        :return: tuple, (x,y)-koordinaatti
        """
        cursor = self._connection.cursor()
        cursor.execute(f"select x from stop_coordinates where stop='{stop}'")
        x_coordinate = cursor.fetchone()[0]
        cursor.execute(f"select y from stop_coordinates where stop='{stop}'")
        y_coordinate = cursor.fetchone()[0]
        return (x_coordinate,y_coordinate)

    def stop_type(self, stop):
        """
        metodi palauttaa aseman tyypin
        :param stop: merkkijono, joka kertoo aseman
        :return: merkkijono, joka kertoo aseman tyypin
        """
        cursor = self._connection.cursor()
        cursor.execute(f"select type from stop_coordinates where stop='{stop}'")
        stop_type = cursor.fetchone()[0]
        return stop_type



    def return_all_start_stops(self):
        """
        metodi palauttaa kaikki lähtöasemat
        :return: lista, lähtöasemista
        """
        cursor = self._connection.cursor()
        cursor.execute("select start from track")
        start = cursor.fetchall()
        stops = []
        for stop in start:
            stops.append(stop[0])
        return stops

    def return_all_bottlenecks(self):
        """
        metodi palauttaa kaikki pullonkaulat
        :return: lista, pullonkauloista
        """
        cursor = self._connection.cursor()
        cursor.execute("select stop from stop_coordinates where type='bottleneck'")
        bottlenecks = cursor.fetchall()
        bottlenecks_list = []
        for bottleneck in bottlenecks:
            bottlenecks_list.append(bottleneck[0])
        return bottlenecks_list

    def distance_to_next_stop(self, dest):
        """
        metodi, joka palauttaa etäisyyden seuraavalle asemalle
        :param dest: merkkijono, seuraava asema
        :return: int-arvo, etäisyys
        """
        cursor = self._connection.cursor()
        cursor.execute(f"select distance from track where dest='{dest}'")
        element = cursor.fetchone()[0]
        return element

    def next_stop(self, start):
        """
        metodi joka palauttaa seuraavan aseman
        :param start: merkkijono, nykyinen/lähtö-asema
        :return: merkkijono, seuraava asema
        """
        cursor = self._connection.cursor()
        cursor.execute(f"select dest from track where start='{start}'")
        try:
            element = cursor.fetchone()[0]
        except TypeError:
            return None
        return element

    def speedlimit_to_next_stop(self, dest):
        """
        metodi, joka palauttaa nopeuden seuraavalle asemalle
        :param dest: merkkijono, seuraava asema
        :return: int-arvo, nopeus
        """
        cursor = self._connection.cursor()
        cursor.execute(f"select speedlimit from track where dest='{dest}'")
        element = cursor.fetchone()[0]
        return element
