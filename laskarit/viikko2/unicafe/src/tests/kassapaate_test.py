import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_alustus_raha(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_alustus_myydyt_edulliset(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_alustus_maukkaat(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_osto_kateisella_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000 + 240/100)

    def test_osto_kateisella_edullinen_paluuhinta(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(400),  160)

    def test_osto_kateisella_makeasti_paluuhinta(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500),  100)

    def test_osto_kateisella_edullinen_kasvattaa_ostoja(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_osto_maukkaasti_kasvattaa_ostoja(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_osto_kateisella_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000 +  400/100)

    def test_osto_edullinen_maksu_liian_pieni_kassan_rahamaara(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_osto_edullinen_maksu_liian_pieni_ostojen_lkm(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_osto_edullinen_maksu_liian_pieni_raha_takaisin(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_osto_maukas_maksu_liian_pieni_kassan_rahamaara(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_osto_maukas_maksu_liian_pieni_ostojen_lkm(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_osto_maukas_maksu_liian_pieni_raha_takaisin(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_kortti_toimii_maukkaasti_ostolla_kassa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo_euroina(), 6)

    def test_kortti_toimii_edullisesti_ostolla_kassa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo_euroina(), 10-2.4)

    def test_kortti_toimii_maukkaasti_ostolla_kassan_lkm(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortti_toimii_edullisesti_ostolla_kassan_lkm(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortti_ei_tarpeeksi_rahaa_maukkaasti(self): ## repetitive so do all asserts in one test
        mockKortti = Maksukortti(10)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(mockKortti), False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(mockKortti.saldo_euroina(), 0.1)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_kortti_ei_tarpeeksi_rahaa_edukkaat(self): ## repetitive so do all asserts in one test
        mockKortti = Maksukortti(10)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(mockKortti), False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(mockKortti.saldo_euroina(), 0.1)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_lataus_toimii_kassassa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1010)

    def test_lataus_toimii_kortilla(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kortti.saldo_euroina(), 20)

    def test_lataus_toimii_kassasa_kun_neg(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_lataus_toimii_kortilla_kun_neg(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(self.kortti.saldo_euroina(), 10)