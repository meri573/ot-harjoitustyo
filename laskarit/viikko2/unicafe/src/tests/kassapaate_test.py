import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_aluksi_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_aluksi_oikea_maara_edullisia_lounaita(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_aluksi_oikea_maara_maukkaita_lounaita(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateismaksu_raha_kassassa_kasvaa_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateismaksu_vaihtoraha_oikea_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_myytyjen_lounaiden_maara_kasvaa_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_raha_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_raha_palautetaan_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)

    def test_myytyjen_lounaiden_maara_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.edulliset, 0)



    def test_kateismaksu_raha_kassassa_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateismaksu_vaihtoraha_oikea_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10)

    def test_myytyjen_lounaiden_maara_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_raha_ei_muutu_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_raha_palautetaan_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(230), 230)

    def test_myytyjen_lounaiden_maara_ei_muutu_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(230)
        self.assertEqual(self.kassapaate.maukkaat, 0)