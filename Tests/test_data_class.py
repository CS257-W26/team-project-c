"""Tests for Data.py"""

import unittest
from ProductionCode.data_class import Data
class DataClass(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.test_data = Data()
        ''' test_AL1025 = [2025,10,"AL","Preliminary","382,814","2,289,572","2,434,519",16.72,
                       "274,505","1,869,742","397,623",14.68,"202,443","2,730,802","7,256",7.41,
                       0,0,0,0.00,"859,762","6,890,116","2,839,398",12.48]
        self.test_data.load_price_row(test_AL1025)'''
        self.test_data.load_data()

    
    def test_al_25_price(self):
        self.assertEqual(self.test_data.data_dict["AL2025"]["commercialRevenue"], 2814661)
        self.assertEqual(self.test_data.data_dict["AL2025"]["totalPrice"], 12.57)

    def test_us_23_price(self):
        self.assertEqual(self.test_data.data_dict["US2023"]["commercialSales"], 1408108779)

    def test_mn_24_emission(self):
        self.assertEqual(self.test_data.data_dict["MN2024"]["generation"], 27814120731.0)
        self.assertEqual(self.test_data.data_dict["MN2024"]["thermalOutput"],17095959.0)

    def test_raise_key_error(self):
        with self.assertRaises(KeyError):
            self.test_data.data_dict["Mn"]

class TestGetData(unittest.TestCase):
    def setUp(self):
        self.database = Data()
        self.database.load_data()

    def test_emissions_only(self):
        states = ["MN", "ND"]
        flags = [False, True]

        entries = self.database.get_data(states, flags, 2024)
        self.assertEqual(len(entries), 2)

        for entry in entries:
            self.assertIn("state", entry)
            self.assertIn("year", entry)
            self.assertIn("co2Tons", entry)