import pygame


class Train(pygame.sprite.Sprite):
    def __init__(self, env, train_number, bottleneck, track, user_interface):
        super().__init__()
        self.image = pygame.Surface([user_interface.cell_size, user_interface.cell_size])
        self.image.fill(pygame.Color(255, 0, 0, 255))
        self.name = "Train " + track.start + " - " + track.dest + " - " + train_number
        self.env = env
        self.process = env.process(self.driving(bottleneck, track))
        self.next_stop = track.next_stop(track.start)
        self.rect = self.image.get_rect()
        self.track = track
        self.rect.x = track.start_xy[0]-1
        self.rect.y = track.start_xy[1]-1
        self.user_interface = user_interface

    def driving(self, bottleneck, track):
        last_stop = False
        next_bottleneck = False
        waiting_time = 0
        while True:
            distance_to_stop = track.distance_to_stop(self.next_stop)
            speed = track.speed_to_stop(self.next_stop)
            time_to_stop = distance_to_stop / speed
            one_km = 1/speed
            print(
                f"{self.name}: time {self.env.now:.1f}h -  starting to drive {distance_to_stop} km"
                f"  to {self.next_stop} with {speed} km/h")
            while time_to_stop:
                pygame.event.pump()
                if time_to_stop > one_km:
                    yield self.env.timeout(one_km)
                    self.move_train(time_to_stop, one_km)
                    time_to_stop = time_to_stop - one_km
                else:
                    yield self.env.timeout(time_to_stop)
                    self.move_train(time_to_stop, one_km)
                    time_to_stop = 0

            print(f"{self.name}: time {self.env.now:.1f}h - {self.next_stop} reached")
            if next_bottleneck:
                with bottleneck.request() as req:
                    yield req
                    yield self.env.timeout(0.05)
                    waiting_time += 0.05
                    print(
                        f"{self.name}: time {self.env.now:.1f}h - bottleneck passed")
                    next_bottleneck = False

            if last_stop:
                print(f"{self.name}: trip complete")
                break
            if not last_stop:
                self.next_stop = track.next_stop(self.next_stop)
                if self.next_stop == self.track.dest:
                    last_stop = True
                if self.track.track_repository.stop_type(self.next_stop) == 'bottleneck':
                    next_bottleneck = True

    def reaching_bottleneck(self):
        while True:
            time_to_bottleneck = 1
            while time_to_bottleneck:
                yield self.env.timeout(time_to_bottleneck)
                print(f"{self.name}: time {self.env.now:.1f}h - bottleneck reached")
                self.process.interrupt()
                time_to_bottleneck = 0
            break

    def move_train(self, time_to_stop, one_km):
        direction = self.next_stop.split('-')[1]
        if time_to_stop < one_km:
            multiplier = time_to_stop/one_km
        else:
            multiplier = 1

        if direction == 'P':
            d_x = 0
            d_y = -1 * multiplier
        elif direction == 'E':
            d_x = 0
            d_y = 1 * multiplier
        self.rect.move_ip(d_x*self.user_interface.cell_size, d_y*self.user_interface.cell_size)
        self.user_interface.all_sprites.draw(self.user_interface.display)
        pygame.display.update()
