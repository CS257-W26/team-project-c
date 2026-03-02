'''Tests for core'''
import unittest
import importlib
from unittest.mock import patch

with patch("ProductionCode.data_source.DataSource.__init__", return_value=None):
    import ProductionCode.core as core

class TestCore(unittest.TestCase):
    '''Tests for core'''

    def setUp(self):
        '''Patches Datasource'''

        self.patcher = patch("ProductionCode.core.db")
        self.mock_data = self.patcher.start()
        self.addCleanup(self.patcher.stop)

        self.mock_data.get_us_year_data.return_value = {
            "state": "US",
            "year": 2014,
            "transportationPrice": 17.38
        }

        self.mock_data.get_states_data.return_value = [{
            "state": "MN",
            "year": 2020,
            "totalSales": 14,
            "residentialPrice": 20.00
        }]

        self.mock_data.get_comparison.return_value = [
            {"state": "IA", "year": 2015, "totalSales": 100},
            {"state": "FL", "year": 2015, "totalSales": 200},
            {"state": "comparison", "totalSales": 100}
        ]

    def test_get_us_data(self):
        '''tests that getting us data works'''
        response = core.get_us_year_data(2014)
        self.assertEqual('17.38', response['transportationPrice'])

    def test_single_state(self):
        """tests that single state returns json for valid input"""
        response = core.get_state_year_data('MN', 2020)
        self.assertEqual("MN", response['state'])
        self.assertEqual('14', response['totalSales'])

    def test_multi_state_comparison(self):
        """tests two state comparison"""
        response = core.get_comparison('IAFL', 2015)
        self.assertEqual("IA", response[0]['state'])
        self.assertEqual("FL", response[1]['state'])
        self.assertEqual("comparison", response[2]['state'])

if __name__ == "__main__":
    unittest.main()
