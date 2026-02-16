"""Tests for TableMaker class"""

import unittest
from ProductionCode.table_maker import TableMaker
from Tests.test_constants import VALID_TABLE#,VALID_MN_TABLE,VALID_US_PRICE_TABLE

class TestTableMakerInput(unittest.TestCase):
    """Tests the TableMaker class input functions"""
    def setUp(self):
        """setup"""
        self.table = TableMaker()
    def test_add_new_empty_entry(self):
        """test add_new_empty_entry function"""
        self.table.add_new_empty_entry('MN', "2025")
        self.assertEqual(self.table.entries[-1].get("state"), "MN")
        self.assertEqual(self.table.entries[-1].get("year"), "2025")
    def testfail_add_new_empty_entry(self):
        """test add_new_empty_entry function fail cases"""
        self.table.add_new_empty_entry('MN', "2025")
        with self.assertRaises(KeyError):
            self.table.add_new_empty_entry('MN', "2025")
    def test_add_new_entry(self):
        """test add_new_entry function"""
        self.table.add_new_entry({'state':'MN', 'year':'2025', 'totalPrice':'25.6'})
        self.assertEqual(self.table.entries[-1].get("state"), "MN")
        self.assertEqual(self.table.entries[-1].get("year"), "2025")
        self.assertEqual(self.table.entries[-1].get("totalPrice"), "25.6")
    def testfail_add_new_entry(self):
        """test add_new_entry function fail cases"""
        with self.assertRaises(TypeError):
            self.table.add_new_entry("dict")
        self.table.add_new_entry({'state':'MN', 'year':'2025', 'totalPrice':'25.6'})
        with self.assertRaises(KeyError):
            self.table.add_new_entry({'state':'MN', 'year':'2025', 'co2Tons':'5000'})
    def test_add_data_for_entry(self):
        """test add_data_for_entry function"""
        self.table.add_new_empty_entry('MN', "2025")
        self.assertEqual(self.table.entries[-1].get("state"), "MN")
        self.assertEqual(self.table.entries[-1].get("year"), "2025")
        self.table.add_data_for_entry('MN', '2025', ('co2Tons', '5000'))
        self.assertEqual(self.table.entries[-1].get("co2Tons"), "5000")
    def testfail_add_data_for_entry(self):
        """test add_data_for_entry function fail cases"""
        self.table.add_new_empty_entry('MN', "2025")
        with self.assertRaises(TypeError):
            self.table.add_data_for_entry('MN', "2024", {'co2Tons': '5000'})
        with self.assertRaises(KeyError):
            self.table.add_data_for_entry('MN', "2024", ('co2Tons', '5000'))

class TestTableMakerOutput(unittest.TestCase):
    """Test the TableMaker class output functions"""
    maxDiff=None
    def setUp(self):
        """setup"""
        self.table = TableMaker()
        self.table.add_new_entry({"state": "MN", "year": "1990"})
        self.table.add_new_entry({"state": "WY", "year": "2005" , "totalRevenue" : 1.2})
        self.table.add_new_empty_entry("US", "2026")
        self.table.add_data_for_entry("US", "2026", ("co2Tons", 50000000))
        self.table.add_data_for_entry("MN", "1990", ("totalFuelConsumptionGeneration", 100))
    def test_get_col_sizes(self):
        """test get_col_sizes function"""
        self.assertEqual(self.table.get_col_sizes(), [5,5,11])
    def test_is_row_empty(self):
        """test is_row_empty function"""
        self.assertFalse(self.table.is_row_empty('co2Tons'))
        self.assertTrue(self.table.is_row_empty('generation'))
    def test_get_table(self):
        """test a simple get_table"""
        output = self.table.get_table().strip()
        self.assertEqual(output, VALID_TABLE)

if __name__ == '__main__':
    unittest.main()
