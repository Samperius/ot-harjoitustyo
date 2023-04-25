
class Track:
    def __init__(self, start, dest, track_repository):
        self.track_repository = track_repository
        self.start_xy = track_repository.station_xy_coordinates(start)
        self.start = start
        self.dest = dest
        self.bottlenecks = track_repository.return_all_bottlenecks()

    def next_stop(self, current_stop):
        return self.track_repository.next_stop(current_stop)

    def speed_to_stop(self, next_stop):
        return self.track_repository.speedlimit_to_next_stop(next_stop)

    def distance_to_stop(self, next_stop):
        return self.track_repository.distance_to_next_stop(next_stop)
