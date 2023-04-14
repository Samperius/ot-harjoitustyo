from repositories.track_repository import Track_repository
import simpy

def generate_trains(level, Train, env, n_trains, start, dest, bottleneck, track, DEFAULT_IMAGE_SIZE):
    trains = []
    for i in range(n_trains):
        train = Train(env, f"Train {i+1}", start, dest, bottleneck, track, DEFAULT_IMAGE_SIZE)
        print(f"pääsitkö tänne?")
        print(train.image)
        level.draw_train(train)
        trains.append(train)
    return trains

def simulate(level, Track, Train, n_trains, DEFAULT_IMAGE_SIZE):
    #params:
    # Dummy data to enable development:
    #muista konffata dirnamet
    #dirname = os.path.dirname(__file__)

    stops = ["Helsinki", "Pasila", "Tikkurila", "Hämeenlinna",
             "Tampere"]  # this data should be imported from database - to be modified later
    speed_limit = {"Pasila": 60, "Tikkurila": 70, "Hämeenlinna": 120,
                   "Tampere": 100}  # this data should be imported from database - to be modified later
    distances = {"Pasila": 5, "Tikkurila": 15, "Hämeenlinna": 100,
                 "Tampere": 100}  # this data should be imported from database - to be modified later

    env = simpy.rt.RealtimeEnvironment(initial_time=0, factor=1.0, strict=True)
    #To-do: Useampi bottleneck
    bottleneck = simpy.PreemptiveResource(env, capacity=1)
    track_repository = Track_repository()
    track = Track("Helsinki", "Tampere", stops, speed_limit, distances, track_repository)
    trains = generate_trains(level, Train,env, n_trains, "Helsinki", "Tampere", bottleneck, track, DEFAULT_IMAGE_SIZE)
    #train2 = Train2(env, f"Train joku", "Helsinki", "Tampere", bottleneck, track)
    env.run(until=3)