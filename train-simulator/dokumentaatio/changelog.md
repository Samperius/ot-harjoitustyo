## Viikko 3
- Rungot luokille Train, Bottleneck ja Track luotu
- Train luokalle luotu yksinkertaistettu simulaatiomalli
- Track- luokalle luotu init-toiminnallisuus ja seuraavan pysäkin, ajonopeuden ja matkan palauttavat metodit. Tämä tullaan myöhemmin integroimaan tietokantaan, josta reittitiedot saadaan.
- Bottleneck-luokan perustiedot määritetty
- Luotu yksinkertaistettu Helsinki-Tampere reitti Train ja Simulate -funktioiden kautta, jolla saatu testiajettua SimPy-kirjaston toimintaa. huom. koodi sisältää vielä tulostuksia, joista tullaan tulevina viikkoina siirtymään Tkinter-UI.n käyttöön
- Luotu track_test.py, joka testaa, että radan nimeämisen ja seuraavan pysäkin palautuksen

## Viikko 4
- Train ja track luokat toteutettu
- Simulaation alustava visualisointi toteutettu pygamen päälle. Tätä varten luotu Level-luokka ja tarvittavat spritet.
- Mahdollistettu useamman junan simulointi yhtäaikaa, jota varten toteutettu generate_train()-funktio.
- Lisätty track_test-kattavuutta sekä lisätty train_test.py Train-luokan testausta varten.

## Viikko 5
- sqlite3 tietokanta, sen alustus ja sieltä tiedon haku toteutettu
- mahdollistettu toiminta usealla rataosuudella
- luotu config-tiedosto tiedostojen nimille kovakoodaamisen sijasta
- aloitettu käyttöliittymän menu-window luominen (ei vielä näy käyttäjälle)

## Viikko 6
- Luotu pygame_menu -pohjainen valikko simulaation käynnistykseen ja parametrointiin
- Luotu käyttäjälle mahdollisuus säätää simuloitavien junien määrää
