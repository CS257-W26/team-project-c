"""tests for data_processing module"""

import unittest
from ProductionCode.data_processing import format_string, to_num_or_zero

class TestFormating(unittest.TestCase):
    """tests data_processing module formating functions"""
    def test_format_string(self):
        """test format_string function"""
        self.assertEqual(format_string('4000'), '4,000')
        self.assertEqual(format_string('63.6432'), '63.64')
        self.assertEqual(format_string('str'), 'str')

class TestStriping(unittest.TestCase):
    """Tests functions used for stripping and converting data to numerics"""
    def test_to_num_or_zero(self):
        """tests the to_num_or_zero function"""
        self.assertEqual(to_num_or_zero('3,000'), 3000)
        self.assertEqual(to_num_or_zero(''), 0)
