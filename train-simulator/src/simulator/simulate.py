
import simpy

def simulate(Track, Train):
    #Dummy data to enable development:
    stops = ["Helsinki", "Pasila", "Tikkurila", "Hämeenlinna",
                  "Tampere"]  # this data should be imported from database - to be modified later
    speed_limit = {"Pasila": 60, "Tikkurila": 70, "Hämeenlinna": 120,
                        "Tampere": 100}  # this data should be imported from database - to be modified later
    distances = {"Pasila": 5, "Tikkurila": 15, "Hämeenlinna": 100,
                      "Tampere": 100}  # this data should be imported from database - to be modified later

    env = simpy.Environment()
    bottleneck = simpy.PreemptiveResource(env, capacity=1)
    track = Track("Helsinki", "Tampere", stops, speed_limit, distances)
    train = Train(env, "Pendolino 1", "Helsinki", "Tampere", bottleneck, track)
    env.run(until=3)


