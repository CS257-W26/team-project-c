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
    def test_get_comparison_table(self):
        """test the comparison table get function"""
        self.table.add_data_for_entry("MN", "1990", ("co2Tons", 40000000))
        output = self.table.get_table().strip()
        self.assertIn("+10,000,000", output, "error in comparison")

# class TestTableOutputUserStories(unittest.TestCase):
#     """Tests for user stories"""
#     maxDiff=None
#     def setUp(self):
#         """setup"""
#         self.database = Data()
#         self.database.load_data()
#     def test_us_display(self):
#         """test displaying us data"""
#         us_price_data = self.database.get_data(["US"], [True, False], 2024)
#         us_table = TableMaker()
#         us_table.add_new_entry(us_price_data[0])
#         output = us_table.get_table().strip()
#         self.assertEqual(output, VALID_US_PRICE_TABLE)
#     def test_two_state_display(self):
#         """test two state display"""
#         two_state_data = self.database.get_data(["ND", "SD"], [True, True], 2024)
#         two_state_table = TableMaker()
#         two_state_table.add_new_entry(two_state_data[0])
#         two_state_table.add_new_entry(two_state_data[1])
#         output = two_state_table.get_comparison_table().strip()
#         self.assertIn("-21,829,505,185", output, "generation difference not present")
#         self.assertIn("+3.35", output, "commercial price difference not present")
#     def test_single_state_display(self):
#         """test single state display"""
#         one_state_data = self.database.get_data(["MN"], [True, True], 2024)
#         one_state_table = TableMaker()
#         one_state_table.add_new_entry(one_state_data[0])
#         output = one_state_table.get_table().strip()
#         self.assertEqual(output, VALID_MN_TABLE)


if __name__ == '__main__':
    unittest.main()
