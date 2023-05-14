# Ohjelmistotekniikka, harjoitustyö
## Lyhyt kuvaus
Sovelluksen avulla pystytään simuloimaan junaverkoston liikennemääriä ja verkoston pullonkaulakohtiin liittyvää junien turhaa odotusaikaa. 

## Releaset
 [viikko 5 release](https://github.com/Samperius/ot-harjoitustyo/releases/tag/viikko7)

## Dokumentaatio
[Työaikakirjanpito](https://github.com/Samperius/ot-harjoitustyo/blob/main/train-simulator/dokumentaatio/tyoaikakirjanpito.md)

[Vaatimusmäärittely](https://github.com/Samperius/ot-harjoitustyo/blob/main/train-simulator/dokumentaatio/vaatimusmaarittely.md)

[Changelog](https://github.com/Samperius/ot-harjoitustyo/blob/main/train-simulator/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/Samperius/ot-harjoitustyo/blob/main/train-simulator/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/Samperius/ot-harjoitustyo/blob/main/train-simulator/dokumentaatio/kaytto-ohje.md)

## Asennus

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

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```


