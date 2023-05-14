# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksen avulla pystytään simuloimaan junien kulkua ohjelmalle määritetyssä junaverkossa.  Olennaisia simulaatioissa ovat ns. pullonkaulakohdat. Junaradan pullonkaulakohtia ovat paikat, joissa ei ole rataa kuin yhdelle junalle kerrallaan. Pohjimmillaan kyseessä on prototyyppi, jolla osoitetaan, että junaradan pullonkaulakohtien vaikutusta junien kulkuun tai viivästymisiin on mahdollista kvantifioida simulaattorin avulla.

## Käyttäjät

Alkuvaiheessa sovelluksella on ainoastaan yksi käyttäjärooli: normaali käyttäjä.	

## Perusversion tarjoama toiminnallisuus 

### Avaintiedot 
- Ohjelma etenee kolmen näkymän välillä valikko-simulaationäkymä-tallennusvalikko.
- Ohjelmaan ei tarvitse kirjautua
- Ohjelma lukee csv-tiedostossa määritellyn rataverkon, tallentaa sen tietokantaan ja generoi radalle käyttäjän määrittelemän määrän junia.
- Ohjelmalla voi ajaa n määrän testiskenaarioita haluamallaan junamäärällä.
- Ohjelmalla voi tallettaa testiskenaarioita csv-muodossa.

## Simulaatio
- Rataverkossa jokaiselle asemavälille on määritetty etäisyys ja sallittu kulkunopeus.
- Ohjelma simuloi junan kulkua rataosuudella:
	- Juna liikkuu sallitulla nopeudella
	- Radan pullonkaulakohdista kulkee yksi juna kerrallaan, ja muut odottavat vuoroaan
	- Juna kulkee pysäkiltä toiselle kunnes saavuttaa määränpäänsä
	- Useampien junien simulointi on mahdollista
- Ohjelma laskee simulaatioiden pohjalta:
	- verkoston pullonkaulojen aiheuttaman odotusajan eli hukan 

## Käyttöliittymä:
- Käyttöliitymässä käyttäjän on mahdollista valita haluamansa junien ja simulaatioiden määrä.
	- Yksittäinen simulaatio on mahdollista animoida yksinkertaiseen koordinaatistoon.
- Käyttöliittymä visualisoi junien kulun asemien välillä ja mahdollistaa yksinkertaisen simuloinnin kuten kuvattu ylempänä.
- Simulaation jälkeen ohjelma näyttää tulokset ja mahdollistaa tallentamisen.

## Jatkokehitysideoita
- Junien simulointi aikataulujen mukaisesti.
- Asemille voisi luoda rajoitetun kapasiteetin, jolloin myös asemien kapasiteettia pystyisi testaamaan.
- Ohjelma voisi hakea simulaation pohjaksi perustiedot junaliikenteestä digitraffic.fi sivulta hyödyntäen avoimen datan GraphQL-rajapintaa
	- Kuinka paljon junia ratavälillä keskimäärin liikkuu
	- mikä on junien nopeus eri vaiheissa rataa
	- mahdollisesti muita parametreja simuloinnin tueksi (tarkentuu myöhemmin)
- Ohjelmaa voisi jatkokehittää, niin että se automaattisesti etsisi optimaalista logiikkaa, jolla junat tulisi ohjata pullonkaulakohtien läpi, niin että päästäisiin pienimpään mahdolliseen odotusaikaan eli hukkaan.(Reinforcement Learning).

