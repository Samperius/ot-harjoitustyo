import simpy


class Bottleneck:
    """
    Luokka kuvaa junaverkossa olevaa pullonkaulaa

    Attributes
    track_name: merkki_jono ,joka kuvaa radan nimeä alusta loppuun "start-stop".
    distance_from_start: int-arvo ,joka kuvaa kilometreissä kuinka kaukana lähtöpisteestä pullonkaula on.
    capacity: int-arvo ,joka kuvaa kuinka monta junaa pullonkaulasta kerralla mahtuu läpi.
    """

    def __init__(self, env, track_name, distance_from_start, capacity):
        self.env = env
        self.track_name = track_name
        self.distance_from_start = distance_from_start
        self.capacity = simpy.PreemptiveResource(env, capacity=1)
