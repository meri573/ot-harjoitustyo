import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_aluksi_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_aluksi_oikea_maara_edullisia_lounaita(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_aluksi_oikea_maara_maukkaita_lounaita(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
