import pygame
import simpy
from repositories.track_repository import TrackRepository
from database_connection import get_database_connection
from entities.track import Track
from entities.train import Train


def generate_trains(user_interface, env, n_trains, bottleneck, track, game_loop):
    trains = []
    for i in range(n_trains):
        train = Train(env, f"{i+1}", bottleneck, track, user_interface, game_loop, False)
        user_interface.draw_train(train)
        trains.append(train)

def simulate(user_interface, n_trains, game_loop):
    #env = simpy.rt.RealtimeEnvironment(initial_time=0, factor=0.001, strict=False)
    env = simpy.Environment()
    bottleneck = simpy.PreemptiveResource(env, capacity=1)
    connection = get_database_connection()
    track_repository = TrackRepository(connection)
    #actual routes to be specified in the start menu by user (TO-DO)
    track = Track("Helsinki-P", "Tampere-P", track_repository)
    generate_trains(user_interface, env, n_trains, bottleneck, track, game_loop)
    track = Track("Tampere-E", "Helsinki-E", track_repository)
    generate_trains(user_interface, env, n_trains, bottleneck, track, game_loop)
    track = Track("Jyväskylä-E", "Helsinki-E", track_repository)
    generate_trains(user_interface, env, n_trains, bottleneck, track, game_loop)
    env.run(until=5)


class Simulation:
    def __init__(self, user_interface, n_trains, game_loop):
        self.n_trains = n_trains
        connection = get_database_connection()
        self.track_repository = TrackRepository(connection)
        self.game_loop = game_loop
        self.user_interface = user_interface

    def generate_train(self, track, name, animate):
        train = Train(self.env, name, self.bottleneck, track, self.user_interface, self.game_loop, animate)
        train.start()
        self.user_interface.draw_train(train)
        return train

    def simulate_once(self, animate):
        self.env = simpy.Environment()
        self.bottleneck = simpy.PreemptiveResource(self.env, capacity=1)
        track = Track("Helsinki-P", "Tampere-P", self.track_repository)
        trains = []
        for i in range(self.n_trains):
            trains.append(self.generate_train(track, f"{i+1}", animate))
        self.env.run(until=3)
        total_wait_time = 0
        for train in trains:
            total_wait_time += train.waiting_time
        print("total: ", total_wait_time)
        return total_wait_time

    def simulate_many(self, n_simulations):
        total_wait_times = []
        for sim in range(n_simulations):
            print(f"starting simulation {sim+1}")
            total_wait_times.append(self.simulate_once(animate = False))
        print(f"{n_simulations} simulations completed")
        self.game_loop.running = False
        return total_wait_times

    def simulate_animated(self):
        total_wait_time = self.simulate_once(animate=True)
        self.game_loop.running = False
        return total_wait_time
