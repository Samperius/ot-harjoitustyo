# Testausdokumentti

Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaavat Track ja Train on testattu niiltä osin, kun se ei vaadi simulaation ajamista ja voi johtaa siihen, että testi menee välillä läpi ja välillä ei (prosessi on osin stokastinen).

### Repositorio-luokat
 
Repositorio-luokan `TrackRepository` alustaminen tallentaa tietoja (radan arkkitehtuurin) SQLite-tietokantaan. Tiedon tallennuksen onnistuminen testataan
 [TestInitializeDatabase](https://github.com/Samperius/ot-harjoitustyo/blob/main/train-simulator/src/tests/database_test.py)-testiluokalla on ja tiedon noutamisen oikeellisuus testataan 
 [TestTrackRepository](https://github.com/Samperius/ot-harjoitustyo/blob/main/train-simulator/src/tests/track_repository_test.py)-testiluokalla.
 
 Tuloksien tallennusta testataan 'test_results.csv'-tiedoston ja [TestSaving](https://github.com/Samperius/ot-harjoitustyo/blob/main/train-simulator/src/tests/saving_test.py)-testiluokan avulla.

### Testauskattavuus

Käyttöliittymäkerrosta ja simulaatiota lukuunottamatta sovelluksen testauksen haarautumakattavuus on 70%

![](https://github.com/Samperius/ot-harjoitustyo/blob/main/train-simulator/dokumentaatio/dokumentaation%20kuvat/coverage.png)

Testauskattavuutta olisi voinut parantaa testaamalla myös simulaation ajaminen siitä huolimatta, vaikka simulaatio ei satunnaisuuden takia tuotakkaan aina samoja tuloksia ja on siten vaikeasti testattavissa.

## Simulaation testaus
Simulaatio on testattu manuaalisesti hyödyntämällä simulaation animointia ja tulostuksia

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu [käyttöohjeen](https://github.com/Samperius/ot-harjoitustyo/blob/main/train-simulator/dokumentaatio/kaytto-ohje.md) kuvaamalla tavalla Linux-ympäristössä. Testauksessa on käytetty myös eri konfiguraatioita _.env_-tiedoston kautta.

### Toiminnallisuudet

Kaikki [määrittelydokumentin](https://github.com/Samperius/ot-harjoitustyo/blob/main/train-simulator/dokumentaatio/vaatimusmaarittely.md) ja käyttöohjeen listaamat toiminnallisuudet on käyty läpi. Syötekenttien toiminta on testattu eri arvoilla huomioiden ääripäät.

## Sovellukseen jääneet laatuongelmat

Sovellus ei anna tällä hetkellä järkeviä virheilmoituksia, seuraavissa tilanteissa:
- Train-luokan driving-metodi tulisi refaktoroida ja pilkkoa paremmin muokattavaan ja ymmärrettävään muotoon.
