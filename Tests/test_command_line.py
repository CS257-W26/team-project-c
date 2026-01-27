'''
File contains tests for command_line.py 
'''
import unittest
from command_line import get_price_data, getEmissionData, getData
import sys
from io import StringIO
from command_line import main

if __name__ == '__main__':
    unittest.main()

class commandLineTestRW(unittest.TestCase):
    maxDiff=None
    def test_get_price_data_KS25(self):
        '''
        Docstring for test_get_price_data_KS25
        Test getPriceData function from command_line.py
        :param self: Description
        '''
        data_ks24 = get_price_data("KS")
        self.assertEqual(data_ks24["residentialRevenue"],1769141)
        self.assertEqual(data_ks24["totalPrice"], 11.46)
        self.assertEqual(data_ks24["commercialSales"],13728250)
    def test_get_us_data(self):
        '''
        Docstring for test_get_us_data
        Test get_price_data for US function from command_line.py
        :param self: Description
        '''
        usData = get_price_data("US")
        self.assertEqual(usData["state"], "US")
        self.assertEqual(usData["commercialSales"], 1246808835)
        self.assertEqual(usData["transportationPrice"], 12.13)
class TestCommandLine(unittest.TestCase):
    def test_normal_query(self):
        """test a valid state in the command line interface"""

class TestGetEmissionData(unittest.TestCase):
    def test_valid_state(self):
        data = getEmissionData("MN")
        self.assertIsInstance(data, dict)
        for k in ["generation", "thermalOutput", "totalFuelConsumption",
                  "totalFuelConsumptionGeneration", "co2Tons", "co2MetricTons"]:
            self.assertIn(k, data)
    
    def test_invalid_state(self):
        with self.assertRaises(KeyError):
            getEmissionData("XX")
    
    def test_US(self):
        us = getEmissionData("US")
        mn = getEmissionData("MN")
        self.assertGreaterEqual(us["co2Tons"], mn["co2Tons"])

class TestGetData(unittest.TestCase):
    def test_emissions_only(self):
        states = ["MN", "ND"]
        flags = [False, True]

        entries = getData(states, flags)
        self.assertEqual(len(entries), 2)

        for entry in entries:
            self.assertIn("state", entry)
            self.assertIn("year", entry)
            self.assertIn("co2Tons", entry)

    def test_both_flags(self):
        states = ["MN"]
        flags = [True, True]

        entries = getData(states, flags)
        self.assertEqual(len(entries), 1)

        entry = entries[0]
        self.assertIn("co2Tons", entry) 
        self.assertIn("totalPrice", entry)   