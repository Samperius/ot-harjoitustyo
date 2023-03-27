import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        
    def test_luotu_kortti_on_olemassa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kateisosto_edullinen_rahaa_on(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(takaisin, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+240)
    	
    def test_kateisosto_edullinen_ei_rahaa(self):
    	takaisin = self.kassapaate.syo_edullisesti_kateisella(200)
    	self.assertEqual(takaisin, 200)
    	self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
 
    def test_kateisosto_maukas_rahaa_on (self):
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(takaisin, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+400)

    def test_kateisosto_maukas_rahaa_ei (self):
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(takaisin, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
  
    def test_korttiosto_edullinen_rahaa_on (self):
    	vastaus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
    	self.assertEqual(vastaus, True)
    	self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")      
    
    def test_korttiosto_edullinen_rahaa_ei_ole (self):
        saldo_ennen = self.kassapaate.edulliset
        self.maksukortti.ota_rahaa(900)
        vastaus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        saldo_jälkeen = self.kassapaate.edulliset
        self.assertEqual(saldo_ennen, saldo_jälkeen)
        self.assertEqual(vastaus, False)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 1.00 euroa")
        
    def test_korttiosto_myytyjen_saldo_edullinen_rahaa_on (self):
    	saldo_ennen = self.kassapaate.edulliset
    	vastaus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
    	saldo_jälkeen = self.kassapaate.edulliset
    	self.assertEqual(saldo_ennen, saldo_jälkeen-1)
   
    def test_korttiosto_edullinen_rahamaara_ei_muutu (self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_korttiosto_maukas_rahaa_on (self):
    	vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
    	self.assertEqual(vastaus, True)
    	self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")   
    	
    def test_korttiosto_myytyjen_saldo_maukas_rahaa_on (self):
    	saldo_ennen = self.kassapaate.maukkaat
    	vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
    	saldo_jälkeen = self.kassapaate.maukkaat
    	self.assertEqual(saldo_ennen, saldo_jälkeen-1)   
    
    def test_korttiosto_maukas_rahaa_ei_ole (self):
        saldo_ennen = self.kassapaate.maukkaat
        self.maksukortti.ota_rahaa(900)
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        saldo_jälkeen = self.kassapaate.maukkaat
        self.assertEqual(saldo_ennen, saldo_jälkeen)
        self.assertEqual(vastaus, False)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 1.00 euroa")

    def test_korttiosto_maukkaasti_rahamaara_ei_muutu (self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortille_lataus (self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")
 
    def test_kortille_0_lataus (self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
 
    def test_kortille_minus_lataus (self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
 

    
