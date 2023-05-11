# Arkkitehtuurikuvaus
## Luokat ja rakenne
Ohjelma noudattaa 3-tasoista kerrosarkkitehtuuria. Sen pakkaukset ovat:
- entities(track, train), joka vastaa radan ja junan toiminnallisuudesta
- repositories(saving, track_repository), joka vastaa tulosten tallennuksesta ja tietokannan muodostamisesta rata-arkkitehtuurille
- simulator(simulator), joka vastaa simulaation ajamisesta kutsuen Track ja Train -luokkia
- Ui(game_loop, menu, run_ui, static_sprites, ui), joka vastaa käyttöliittymästä valikoiden ja simulaation osalta.

Ohjelman luokkien suhdetta kuvaa luokkakaavio:
```mermaid
classDiagram
 Ui -- StaticSprite
 Ui -- Train
 Track -- Train
 Track -- TrackRepository
 Simulator -- Track
 Track -- Train
 Train -- SimPy
 Ui -- Saving

 class Ui{
 trains
 tracks
 forests
 stops
 bottlenecks
 all_sprites
 MAP
 
 }
 class StaticSprite{
 image
 rect.x
 rext.y
 }
 
 class Track{
 track_repository
 start_xy
 start
 dest
 next_stop()
 speed_to_stop()
 distance_to_stop()
 }
 
 class Train{
 image
 env
 name
 next_stop
 rect
 user_interface
 game_loop
 draw_or_not
 waiting_time
 start()
 driving()
 user_message()
 move_train()
  }
  
 class TrackRepository{
 connection
 station_xy_coordinates()
 stop_type()
 return_all_start_stops()
 return_all_bottlenecks()
 distance_to_next_stop()
 next_stop()
 speedlimit_to_next_stop() 
 }
 
 class Simulator{
 n_trains
 track_repository
 game_loop
 user_interface
 generate_train()
 simulate_once()
 simulate_many()
 simulate_animated()
 }
 
 class Saving{
 RESULTS_PATH
 file_exists
 save_dataframe()
 }
 class SimPy{
 env
 bottleneck
 env.process()
 env.timeout()
 bottleneck.request
 }
 
 ```
## Päätoiminnallisuudet
Ohjelmalogiikka etenee simulaation aloituksesta tallennukseen seuraavasti:

```mermaid
sequenceDiagram
  actor User
  
  participant menu
  participant run_ui
  participant Ui
  participant Simulator
  participant Track
  participant Train
  participant SimPy
  participant Saving

  User->>menu: adjust "number of trains" slider
  User->>menu: click "simulation" button
  menu->>run_ui: animate_single_simulations(number of trains)
  run_ui->>Ui: _initialize_sprites(self, MAP)
  run_ui->>Simulation: simulate_animated()
  run_ui->>GameLoop: start()
  Simulator->> Track: init()
  Simulator->>Train: train.start()
  Train->>Simpy: env.process(train.driving(bottleneck, track))
  Simulator->>Ui: draw_train()
  Train->>Ui: rect.move_ip(dx, dy)
  Simulator->>menu: results(saved=False)
  menu->>Saving: save_dataframe(data)
``` 
## Tiedostot
Ohjelma tallentaa simulaatioiden tulokset erilliseen oletuksena "results.csv" -nimiseen tiedostoon. 

Ohjelma hakee rata-arkkitehtuurin oletuksena "track.csv"- ja "stop_coordinates.csv" -nimisistä tiedostoista. Näiden tiedostot pohjalta initialize_database() luo SQLite tietokantataulun track ja stop_coordinates. Nämä tiedostot korvaamalla ja uudelleen alustamalla on mahdollista kustomoida uusia ratoja. Tiedostojen muodon tulee säilyä identtisenä.

Sovelluksen juureen sijoitettu konfiguraatiotiedosto .env määrittelee tiedoston nimet.

## Ohjelman rakenteeseen jääneet heikkoudet
### Käyttöliittymän valikko
- Valikkoa ei ole toteutettu luokiksi, koska se aiheutti ongelmia pygame_menu-kirjaston toiminnan kanssa. 
- Valittu kirjasto vaati nappien taakse invoke funktiot(ilman parametreja), jolloin muuttujia ei pystynyt injektoimaan metodien välille. Tästä syystä menu-tiedostossa käytetään globaaleja muuttujia.
