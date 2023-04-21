
class Track:
    def __init__(self, start, dest, stops, speed_limit, distances, track_repository):
        # naming tracks allows expanding program to multiple tracks
        self.name = "-".join((start, dest))
        self.track_repository = track_repository
        self.start_xy = track_repository.station_xy_coordinates()
        self.start = start
        self.dest = dest
        # this data should be imported from database - to be modified later
        self.stops = stops
        self.speed_limits = speed_limit
        self.distances = distances
        self.bottlenecks = []  # bottlenecks counted based on distance from the start
    # returns the distance to the next bottleneck

    def next_stop(self, current_stop):
        return self.track_repository.next_stop(current_stop)
        next_stop_indx = self.stops.index(current_stop)+1
        if next_stop_indx == len(self.stops):
            return self.stops[-1]
        if next_stop_indx != len(self.stops):
            return self.stops[next_stop_indx]

    def speed_to_stop(self, next_stop):
        return self.track_repository.speedlimit_to_next_stop(next_stop)

    def distance_to_stop(self, next_stop):
        return self.track_repository.distance_to_next_stop(next_stop)