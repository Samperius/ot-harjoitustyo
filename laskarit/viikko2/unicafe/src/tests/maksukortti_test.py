import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_saldo_on_alussa_oikein(self):
        self.assertEqual(str(Maksukortti(0)), "Kortilla on rahaa 0.00 euroa")
        
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(20000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 210.00 euroa")
        
    def test_rahan_ottaminen_toimii_jos_rahaa(self):
        self.maksukortti.ota_rahaa(900)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 1.00 euroa")

    def test_rahan_ottaminen_toimii_jos_ei_rahaa(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_ottaminen_onnistuminen_palauttaa_truen(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1000), True)
        
    def test_rahan_ottaminen_failure_palauttaa_falsen(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)
