import simpy
import pygame
import numpy as np


class Train(pygame.sprite.Sprite):
    def __init__(self, env, name, start, dest, bottleneck, track, DEFAULT_IMAGE_SIZE):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("./src/visuals/train.png"), DEFAULT_IMAGE_SIZE/2)
        self.env = env
        self.name = name
        self.start = start
        self.dest = dest
        self.cell_size = DEFAULT_IMAGE_SIZE[0]
        self.process = env.process(self.driving(bottleneck, track))
        #env.process(self.reaching_bottleneck())
        self.next_stop = track.next_stop(start)
        self.rect = self.image.get_rect()
        self.rect.x = track.start[0]
        self.rect.y = track.start[1]
        self.timex = 1


    def driving(self, bottleneck, track):
        while True:
            distance_to_stop = track.distance_to_stop(self.next_stop)
            speed = track.speed_to_stop(self.next_stop)
            time_to_stop = distance_to_stop / speed
            print(
                f"{self.name}: time {self.env.now:.1f}h -  starting to drive {distance_to_stop} km  to {self.next_stop} with {speed} km/h")

            while time_to_stop:
                try:
                    start = self.env.now
                    yield self.env.timeout(self.timex*time_to_stop)
                    time_to_stop = 0
                except simpy.Interrupt:
                    time_to_stop = time_to_stop - (self.env.now - start)
                    with bottleneck.request() as req:
                        yield req
                        yield self.env.timeout(self.timex*0.3)
                        print(
                            f"{self.name}: time {self.env.now:.1f}h - time for you to continue, time to destination {time_to_stop:.1f}")
            print(f"{self.name}: time {self.env.now:.1f}h - {self.next_stop} reached")
            if self.next_stop == track.next_stop(self.next_stop):
                print(f"{self.name}: trip complete")
                break
            else:
                self.next_stop = track.next_stop(self.next_stop)
                self.move_train(10,0)

    def reaching_bottleneck(self):
        while True:
            time_to_bottleneck = 1
            while time_to_bottleneck:
                yield self.env.timeout(self.timex*time_to_bottleneck)
                print(f"{self.name}: time {self.env.now:.1f}h - bottleneck reached")
                self.process.interrupt()
                time_to_bottleneck = 0
            break



    def move_train(self, dx=0, dy=0):
        self.rect.move_ip(dx*self.cell_size, dy*self.cell_size)
