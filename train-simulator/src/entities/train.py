import simpy


class Train(object):
    def __init__(self, env, name, start, dest, bottleneck, track):
        self.env = env
        self.name = name
        self.start = start
        self.dest = dest
        self.bottleneck = bottleneck
        self.process = env.process(self.driving(bottleneck,track))
        env.process(self.reaching_bottleneck())
        self.next_stop = track.next_stop(start)

    def driving(self, bottleneck, track):
        while True:
            distance_to_stop = track.distance_to_stop(self.next_stop)
            speed = track.speed_to_stop(self.next_stop)
            time_to_stop = distance_to_stop / speed
            print(
                f"Time {self.env.now:.1f}h -  starting to drive {distance_to_stop} km  to {self.next_stop} with {speed} km/h")

            while time_to_stop:
                try:
                    start = self.env.now
                    yield self.env.timeout(time_to_stop)
                    time_to_stop = 0
                except simpy.Interrupt:
                    time_to_stop = time_to_stop - (self.env.now - start)
                    with bottleneck.request() as req:
                        yield req
                        print(
                            f"Time {self.env.now:.1f}h - time for you to continue, time to destination {time_to_stop:.1f}")
            print(f"Time {self.env.now:.1f}h - {self.next_stop} reached")
            if self.next_stop == track.next_stop(self.next_stop):
                print("Trip complete")
                break
            else:
                self.next_stop = track.next_stop(self.next_stop)


    def reaching_bottleneck(self):
        while True:
            time_to_bottleneck = 2
            while time_to_bottleneck:
                yield self.env.timeout(time_to_bottleneck)
                print(f"Time {self.env.now:.1f}h - bottleneck reached")
                self.process.interrupt()
                time_to_bottleneck = 0
            break