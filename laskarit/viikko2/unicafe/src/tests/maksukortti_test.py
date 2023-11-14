import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 15)

    def test_ottaa_kun_riittaa(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 9)

    def test_ei_ota_kun_ei_riita(self):
        self.maksukortti.ota_rahaa(10000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_ota_metodin_paluuarvo(self):
        self.assertEqual(self.maksukortti.ota_rahaa(10), True)

    def test_ota_metodin_paluuarvo2(self):
        self.assertEqual(self.maksukortti.ota_rahaa(10000), False)

    def test_to_string_metodi(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")