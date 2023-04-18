import simpy
from repositories.track_repository import TrackRepository

def generate_trains(level, Train, env, n_trains, start, dest, bottleneck, track):
    trains = []
    for i in range(n_trains):
        train = Train(env, f"Train {i+1}", bottleneck, track, level)
        level.draw_train(train)
        trains.append(train)

def simulate(level, Track, Train, n_trains):
    #params:
    # Dummy data to enable development:
    #muista konffata dirnamet
    #dirname = os.path.dirname(__file__)

    stops = ["Helsinki", "Pasila", "Tikkurila", "Hämeenlinna",
             "Tampere"]  # this data should be imported from database
    speed_limit = {"Pasila": 60, "Tikkurila": 70, "Hämeenlinna": 120,
                   "Tampere": 100}  # this data should be imported from database
    distances = {"Pasila": 5, "Tikkurila": 15, "Hämeenlinna": 60,
                 "Tampere": 100}  # this data should be imported from database

    env = simpy.rt.RealtimeEnvironment(initial_time=0, factor=1.0, strict=False)
    #To-do: Useampi bottleneck
    bottleneck = simpy.PreemptiveResource(env, capacity=1)
    track_repository = TrackRepository()
    track = Track("Helsinki", "Tampere", stops, speed_limit, distances, track_repository)
    generate_trains(level, Train,env, n_trains, "Helsinki", "Tampere", bottleneck, track)
    env.run(until=5)
