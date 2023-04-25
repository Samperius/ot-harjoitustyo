import simpy
from repositories.track_repository import TrackRepository
from database_connection import get_database_connection

def generate_trains(user_interface, Train, env, n_trains, bottleneck, track):
    trains = []
    for i in range(n_trains):
        train = Train(env, f"Train {i+1}", bottleneck, track, user_interface)
        user_interface.draw_train(train)
        trains.append(train)

def simulate(user_interface, Track, Train, n_trains):
    env = simpy.rt.RealtimeEnvironment(initial_time=0, factor=1, strict=False)
    bottleneck = simpy.PreemptiveResource(env, capacity=1)
    connection = get_database_connection()
    track_repository = TrackRepository(connection)
    track = Track("Helsinki-P", "Tampere-P", track_repository)
    generate_trains(user_interface, Train, env, n_trains, bottleneck, track)
    track = Track("Jyväskylä-E", "Helsinki-E", track_repository)
    generate_trains(user_interface, Train, env, n_trains, bottleneck, track)
    env.run(until=5)