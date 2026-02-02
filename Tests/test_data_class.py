"""Tests for Data.py"""

import unittest
from production_code.data_class import Data
class DataClass(unittest.TestCase):
    '''Tests for data class'''
    maxDiff = None

    def setUp(self):
        '''load data into Data object'''
        self.test_data = Data()
        self.test_data.load_data()

    def test_al_25_price(self):
        '''Tests loading of price data'''
        self.assertEqual(self.test_data.data_dict["AL2025"]["commercialRevenue"], 2814661)
        self.assertEqual(self.test_data.data_dict["AL2025"]["totalPrice"], 12.57)

    def test_us_23_price(self):
        '''test loading of us price'''
        self.assertEqual(self.test_data.data_dict["US2023"]["commercialSales"], 1408108779)

    def test_mn_24_emission(self):
        '''test loading of emission data'''
        self.assertEqual(self.test_data.data_dict["MN2024"]["generation"], 27814120731.0)
        self.assertEqual(self.test_data.data_dict["MN2024"]["thermalOutput"],17095959.0)

    def test_raise_key_error(self):
        '''tests that invlaid dict keys cause error'''
        with self.assertRaises(KeyError):
            self.test_data.data_dict["Mn"]

class TestGetData(unittest.TestCase):
    '''test get data functoin'''
    def setUp(self):
        '''load data into data object'''
        self.database = Data()
        self.database.load_data()

    def test_emissions_only(self):
        '''test emmissions only'''
        states = ["MN", "ND"]
        flags = [False, True]

        entries = self.database.get_data(states, flags, 2024)
        self.assertEqual(len(entries), 2)

        for entry in entries:
            self.assertIn("state", entry)
            self.assertIn("year", entry)
            self.assertIn("co2Tons", entry)
