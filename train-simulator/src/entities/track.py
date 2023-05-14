
class Track:
    """
    Luokka, joka toimii ratayhteytenä kommunikoiden Train ja Track_repository-luokkien kanssa

    Attributes:
        track_repository: TrackRepository-luokan olio, joka noutaa radan tiedot SQLite tietokannasta
        start_xy: (x,y) koordinaatti-tuple, joka sisältää tiedon, mistä koordinaatista juna starttaa
        start: merkkijono, joka kertoo junan lähtöaseman
        dest: merkkijono, joka kertoo junan kohdeaseman
    """
    def __init__(self, start, dest, track_repository):
        """
        konstruktorimetodi
        :param start: merkkijono, joka kertoo junan lähtöaseman
        :param dest: merkkijono, joka kertoo junan kohdeaseman
        :param track_repository: TrackRepository-luokan olio, joka noutaa radan tiedot SQLite tietokannasta
        """
        self.track_repository = track_repository
        self.start_xy = track_repository.station_xy_coordinates(start)
        self.start = start
        self.dest = dest

    def next_stop(self, current_stop):
        """
        metodi, joka palauttaa seuraavan aseman nimen
        :param current_stop: merkkijono, joka kertoo nykyisen aseman
        :return: merkkijono, joka kertaa seuraavan aseman
        """
        return self.track_repository.next_stop(current_stop)

    def speed_to_stop(self, next_stop):
        """
        metodi, joka palauttaa nopeuden seuraavalle asemalle
        :param next_stop: merkkijono, joka kertaa seuraavan aseman
        :return: int-arvo, nopeus
        """
        return self.track_repository.speedlimit_to_next_stop(next_stop)

    def distance_to_stop(self, next_stop):
        """
        metodi, joka palauttaa etäisyyedn seuraavalle asemalle
        :param next_stop: merkkijono, joka kertaa seuraavan aseman
        :return:  int-arvo, etäisyys
        """
        return self.track_repository.distance_to_next_stop(next_stop)
