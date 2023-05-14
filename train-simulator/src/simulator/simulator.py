import simpy
from repositories.track_repository import TrackRepository
from database_connection import get_database_connection
from entities.track import Track
from entities.train import Train


class Simulator:
    """
    'Simulaatioluokka, joka luo ja kutsuu yksittäisiä Train-olioita, joissa simulaatio tapahtuu

    Attributes:
    n_train: Number of trains - eli simuloitavien junien lukumäärä
    track_repository: Rataverkko-tietokantaa hallinnoiva olio
    user_interface: käyttöliittymää kuvaava olio, jolle Train-olio syöttää sijaintitietoa.
    game_loop: pelikiertoa kuvaava olio joka käsittelee käyttäjän syötteitä ja päivittää ui.ta
    """
    def __init__(self, user_interface, n_trains, game_loop):
        """
        Luokan konstruktori

        Args:
        param n_train: Number of trains - eli simuloitavien junien lukumäärä
        param user_interface: käyttöliittymää kuvaava olio, jolle Train-olio syöttää sijaintitietoa.
        Tarvitaan vain, jos kyseeessä on animoitava simulaatio. Oletuksena None
        param game_loop: pelikiertoa kuvaava olio joka käsittelee käyttäjän syötteitä ja päivittää ui.ta
        Tarvitaan vain, jos kyseeessä on animoitava simulaatio. Oletuksena None
        """
        self.n_trains = n_trains
        connection = get_database_connection()
        self.track_repository = TrackRepository(connection)
        self.game_loop = game_loop
        self.user_interface = user_interface

    def generate_train(self, track, name, animate):
        """
        Metodi, joka vastaa junien generoimisesta simulaatiota varten.
        :param track: Rataverkkoa kuvaava olio
        :param name: Junan nimi
        :param env: Simpy-environment-olio
        :param bottleneck: Simpy-resource-olio
        :param animate: animoidaanko vai ei, joko True tai False
        :return: palauttaa generoidun Train-olion, jonka simulaatio on käynnistty.
        """
        train = Train(self.env, name, self.bottleneck, track, self.user_interface, self.game_loop, animate)
        train.start()
        self.user_interface.draw_train(train)
        return train


    def simulate_once(self, animate):
        """
        Metodi, vastaa yhden simulaation pyörittämisestä alusta loppuun
        :param animate: Animoidaanko simulaatio, joko True tai False
        :return: palauttaa kyseisen simulaation kokonaisodotusajan/hukan
        """
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
        """
        Metodi, joka vastaa useamman simulaation pyörittämisestä kutsuen simulate_once()-metodia
        :param n_simulations: simulaatioiden lukumäärä
        :return: palauttaa kaikkien simulaatioiden odotusajan/hukan listamuodossa
        """
        total_wait_times = []
        for sim in range(n_simulations):
            print(f"starting simulation {sim+1}")
            total_wait_times.append(self.simulate_once(animate = False))
        print(f"{n_simulations} simulations completed")
        self.game_loop.running = False
        return total_wait_times

    def simulate_animated(self):
        """
        Metodi vastaa animoidun simulaation pyörittämisestä kutsuen simulate_once-metodia
        :return: palautaa simulaation odotusajan/hukan
        """
        total_wait_time = self.simulate_once(animate=True)
        self.game_loop.running = False
        return total_wait_time