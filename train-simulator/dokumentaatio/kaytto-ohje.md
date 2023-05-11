# Käyttöohje
## Käyttöönotto
Jotta saat ohjelman käyttöön, tulee sinun ladata viimeisin release, joka löytyy projektin [etusivun alareunasta](https://github.com/Samperius/ot-harjoitustyo).
Tämän jälkeen sinun tulee asentaa ohjelman vaatimat riippuvuudet ja alustaa ohjelman toiminta seuraavasti:

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Konfigurointi
Junaradan alustuksen ja tallennuksen sekä tulosten tallennuksen tiedostonimiä on mahdollista muuttaa _.env_-tiedostossa
```
DATABASE_FILENAME=TrainSimulator.db
TRACk_INFO_FILENAME = track.csv
STOPS_INFO_FILENAME = stops.csv
STOP_COORDINATE_FILENAME = stop_coordinates.csv
BOTTLENECKS_FILENAME = bottlenecks.csv
RESULTS_FILENAME = results.csv
```
## Simulaattorin käyttö
Simulaattorissa on 3 päätoiminnallisuutta: 1. Animoitu simulaatio 2. Useiden simulaatioiden ajaminen 3. Tulosten tallentaminen

## Alkuvalikko
![](https://github.com/Samperius/ot-harjoitustyo/blob/main/train-simulator/dokumentaatio/dokumentaation%20kuvat/aloitusvalikko.png)

1. Jos haluat tarkastella visuaalisesti, miten simulaatio toimii, niin valitse haluamasi junien määrä liukuria käyttäen ja paina "Animate single simulation"
2. Jos haluat simuloida kerralla useamman simulaation, niin valitse liukureilla junien ja simulaatioiden määrä ja paina "Run multiple simulations".

## Tulokset ja tallennus
![](https://github.com/Samperius/ot-harjoitustyo/blob/main/train-simulator/dokumentaatio/dokumentaation%20kuvat/tulokset%20ja%20tallennus.png)
Average waiting time kertoo, kuinka paljon turhaa odotusta eli hukkaa radan pullonkaulakohdista aiheutui per simulaatio.
Tulokset on mahdollista tallentaa painamalla "save results". Tämä synnyttää Data-kansioon oletuksena _results.csv_-nimisen tiedoston. Tallennuksen jälkeen valikko palaa aloitusvalikkoon, jonka jälkeen on mahdollista suorittaa uusia simulaatioita ja tallentaa tuloksia.

## Lopetus
Ohjelman lopetus tapahtuu painamalla 'Quit' painiketta joko Aloitus- tai Tulos ja tallennus-valikoissa.
Häiriötilanteessa ohjelman voi sammuttaa väkisin myös control+c -yhdistelmällä, mutta tällöin ei tuloksia pysty tarkastelemaan tai tallentamaan vaan on aloitettava alusta.








