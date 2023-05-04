import pygame
import simpy
from repositories.track_repository import TrackRepository
from database_connection import get_database_connection
from entities.track import Track
from entities.train import Train


def generate_trains(user_interface, env, n_trains, bottleneck, track, game_loop):
    trains = []
    for i in range(n_trains):
        train = Train(env, f"{i+1}", bottleneck, track, user_interface, game_loop, True)
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

