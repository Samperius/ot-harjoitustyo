import pygame
import random


class Train(pygame.sprite.Sprite):
    """
        Train-luokka on sovelluslogiikan kannalta tärkein, sillä se vastaa yksittäisen junan toiminnasta

        Attributes:
            name: merkkijono, joka kuvaa junan nimeä
            env: Simpy environment-olio, joka vastaa simulaatioympäristöstä
            bottleneck: Simpy resource-olio, joka vastaa pullonkaulakohtien toiminnasta
            next_stop: merkkijono, joka kuvaa junan seuraavaa kohdeasemaa
            track: Track-luokan olio, joka vastaa radan tiedoista
            draw_or_not: Boolean arvo, joka kuvastaa animoidaanko simulaatio
            waiting time: float-arvo, joka pitää kirjaa odotusajasta/hukasta
            user_interface: Ui-luokan  olio, joka vastaa käyttöliittymästä simulaation osalta
        """
    def __init__(self, env, train_number, bottleneck, track, user_interface, game_loop=False, draw_or_not=False):
        """
        Luokan konstruktori
        :param env: Simpy environment-olio, joka vastaa simulaatioympäristöstä
        :param train_number: int-arvo, joka kuvaa junan numeroa. Käytetään junan nimessä.
        :param bottleneck: Simpy resource-olio, joka vastaa pullonkaulakohtien toiminnasta
        :param track: Track-luokan olio, joka vastaa radan tiedoista
        :param user_interface: Ui-luokan  olio, joka vastaa käyttöliittymästä simulaation osalta
        :param draw_or_not: Boolean arvo, joka kuvastaa animoidaanko simulaatio
        """
        super().__init__()
        self.image = pygame.Surface([user_interface.cell_size, user_interface.cell_size])
        self.image.fill(pygame.Color(255, 0, 0, 255))
        self.name = "Train " + track.start + " - " + track.dest + " - " + train_number
        self.env = env
        self.bottleneck = bottleneck
        self.next_stop = track.next_stop(track.start)
        self.rect = self.image.get_rect()
        self.track = track
        self.rect.x = track.start_xy[0]-1
        self.rect.y = track.start_xy[1]-1
        self.user_interface = user_interface
        self.game_loop = game_loop
        self.draw_or_not = draw_or_not
        self.waiting_time = 0

    def start(self):
        """
        metodi, joka on tarkoitettu Simpy Environmentin prosessin käynnistykseen eli junan liikkeelle lähtöön
        :return:
        """
        self.env.process(self.driving(self.bottleneck, self.track))
        return

    def driving(self, bottleneck, track):
        """
        metodi, joka vastaa junan kulusta asemalta toiselle
        :param bottleneck: Simpy resource-olio, joka vastaa pullonkaulakohtien toiminnasta
        :param track: Track-luokan olio, joka vastaa radan tiedoista
        :return:
        """
        last_stop = False
        next_bottleneck = False
        while True:
            distance_to_stop = track.distance_to_stop(self.next_stop)
            speed = track.speed_to_stop(self.next_stop)
            time_to_stop = distance_to_stop / speed
            one_km = 1/speed
            self.user_message('next_stop', True)
            while time_to_stop:
                if self.draw_or_not:
                    pygame.event.pump()
                if time_to_stop > one_km:
                    yield self.env.timeout(one_km)
                    self.move_train(time_to_stop, one_km)
                    time_to_stop = time_to_stop - one_km
                else:
                    yield self.env.timeout(time_to_stop)
                    self.move_train(time_to_stop, one_km)
                    time_to_stop = 0

            self.user_message('station_reached', True)
            if next_bottleneck:
                with bottleneck.request() as req:
                    waiting_started = self.env.now
                    yield req
                    yield self.env.timeout(random.lognormvariate(0.1,0.05))
                    self.waiting_time += self.env.now - waiting_started
                    self.user_message('bottleneck_passed', True)
                    next_bottleneck = False

            if last_stop:
                self.user_message('trip_complete', True)
                print(self.waiting_time)
                break
            if not last_stop:
                self.next_stop = track.next_stop(self.next_stop)
                if self.next_stop == self.track.dest:
                    last_stop = True
                if self.track.track_repository.stop_type(self.next_stop) == 'bottleneck':
                    next_bottleneck = True


    def user_message(self, command, print_or_not):
        """
        Metodi joka tuottaa käyttäjälle tulosteita
        :param command: merkkijono, joka kertoo mitä käyttäjälle tulostetaan
        :param print_or_not: Boolean arvo, jonka avulla mahdollisuus jättää printit pois
        """
        if print_or_not:
            if command == 'next_stop':
                print(
                f"{self.name}: time {self.env.now:.1f}h -  starting to drive to {self.next_stop}")
            elif command == 'station_reached':
                print(f"{self.name}: time {self.env.now:.1f}h - {self.next_stop} reached")
            elif command == 'bottleneck_passed':
                print(
                    f"{self.name}: time {self.env.now:.1f}h - bottleneck passed")
            elif command == 'trip_complete':
                print(f"{self.name}: trip complete")

    def move_train(self, time_to_stop, one_km):
        """
        metodi, joka kommunikoi käyttöliittymälle junan liikkeet oikeaan suuntaan
        :param time_to_stop: float-arvo, joka kertoo kuinka kauan sallittua nopeutta kestää seuraavalle asemalle
        :param one_km:  float arvo, joka kertoo kuinka kauan yhden kilomoterin ajaminen kestää
        """
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
        if self.draw_or_not:
            self.rect.move_ip(d_x*self.user_interface.cell_size, d_y*self.user_interface.cell_size)
            self.user_interface.all_sprites.draw(self.user_interface.display)
            pygame.display.update()