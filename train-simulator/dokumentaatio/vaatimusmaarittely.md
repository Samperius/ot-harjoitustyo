# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla pystytään simuloimaan junaverkoston liikennemääriä ja verkoston pullonkaulakohtiin liittyvää junien turhaa odotusaikaa. Perusversiossa malllinnetaan ja simuloidaan vain yksi rataväli, mutta jatkokehityksenä / laajennuksena on mahdollista lisätä myös muita ratavälejä.

## Käyttäjät

Alkuvaiheessa sovelluksella on ainoastaan yksi käyttäjärooli eli normaali käyttäjä.	

## Käyttöliittymäluonnos
## Perusversion tarjoama toiminnallisuus 

### Avaintiedot 
- Ohjelmaan ei tarvitse kirjautua - tehty (ei vaadi toimenpiteitä)
- Ohjelmalla voi ajaa n määrän testiskenaarioita haluamillaan parametreilla - työn alla
- Ohjelmalla voi tallettaa testiskenaarioita ja avata aiemmin simuloituja skenaarioita - aloittamatta

## Simulaatio
- Ohjelma simuloi junan kulkua rataosuudella:
	- Juna liikkuu sallitulla nopeudella - **tehty**
	- Radan pullonkaulakohdista kulkee yksi juna kerrallaan, ja muut odottavat vuoroaan - **tehty**
	- Juna kulkee pysäkiltä toiselle kunnes saavuttaa määränpäänsä - **tehty**
	- Useampien junien simulointi on mahdollista - **tehty**
- Ohjelma simuloi annetulle aikavälille liikenteen:
	- Käyttäjä pystyy muuttamaan liikennemääriä suhteessa base-skanaarioon **osin tehty**
	- Käyttäjä pystyy muuttamaan logiikkaa, jolla junat ohittavat pullonkaulakohdat:
		- esim. First In First Out (FIFO) tai First In Last Out (LIFO)
- Ohjelma laskee simulaatioiden pohjalta:
	- verkoston pullonkaulojen aiheuttaman odotusajan eli hukan 

## Käyttöliittymä:
- Käyttöliittymä visualisoi junien kulun asemien välillä ja mahdollistaa yksinkertaisen simuloinnin kuten kuvattu ylempänä. - Yksinkertaistetun käyttöliittymän v.1.0 **tehty**
- Käyttöliittymässä parametrien muuttaminen on mahdollista **osin tehty**

## Jatkokehitysideoita
- Ohjelma voisi hakea simulaation pohjaksi perustiedot junaliikenteestä digitraffic.fi sivulta hyödyntäen avoimen datan GraphQL-rajapintaa
	- Kuinka paljon junia ratavälillä keskimäärin liikkuu
	- mikä on junien nopeus eri vaiheissa rataa
	- mahdollisesti muita parametreja simuloinnin tueksi (tarkentuu myöhemmin)
- Ohjelma on laajennettavissa kattamaan useita ratavälejä. Lopullinen tavoite tulisi olla mallintaa koko rataverkko, sillä liikenteen dynamiikka yhdellä ratavälillä vaikuttaa liikenteeseen muilla rataväleillä. **tehty**
- Ohjelmaa voisi jatkokehittää, niin että se automaattisesti etsisi optimaalista logiikkaa, jolla junat tulisi ohjata pullonkaulakohtien läpi, niin että päästäisiin pienimpään mahdolliseen odotusaikaan eli hukkaan.(Reinforcement Learning)

