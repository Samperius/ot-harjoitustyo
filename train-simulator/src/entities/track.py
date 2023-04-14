import simpy


class Track(object):
    def __init__(self, start, dest, stops, speed_limit, distances, track_repository):
        # naming tracks allows expanding program to multiple tracks
        self.name = "-".join((start, dest))
        self.start = track_repository.station_xy_coordinates(start)
        self.dest = dest
        # this data should be imported from database - to be modified later
        self.stops = stops
        self.speed_limit = speed_limit
        self.distances = distances
        self.bottlenecks = []  # bottlenecks counted based on distance from the start
    # returns the distance to the next bottleneck

    def return_bottleneck(self, current_dist):
        ...

    def next_stop(self, current_stop):
        next_stop_indx = self.stops.index(current_stop)+1
        if next_stop_indx == len(self.stops):
            return self.stops[-1]
        else:
            return self.stops[next_stop_indx]

    def speed_to_stop(self, next_stop):
        return self.speed_limit[next_stop]

    def distance_to_stop(self, next_stop):
        return self.distances[next_stop]
