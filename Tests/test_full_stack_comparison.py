'''Full stack tests for multi-state comparison routes'''
import unittest
from unittest.mock import patch
import flask_app

class TestFullStackComparison(unittest.TestCase):
    '''Full stack comparison tests'''

    def setUp(self):
        self.patcher = patch("ProductionCode.core.DataSource")
        self.mock_class = self.patcher.start()
        self.addCleanup(self.patcher.stop)

        self.mock_db = self.mock_class.return_value

        # Mock the comparison data
        self.mock_db.get_comparison.return_value = [
            {"state": "IA", "year": 2015, "totalSales": 100},
            {"state": "FL", "year": 2015, "totalSales": 200},
            {"state": "comparison", "totalSales": 100}
        ]

        self.client = flask_app.app.test_client()

    def test_multi_state_comparison(self):
        '''tests two state comparison'''
        response = self.client.get("/compare/IAFL?year=2015", follow_redirects=True)
        body = response.get_data(as_text=True)
        self.assertIn("IA", body)
        self.assertIn("FL", body)
        self.assertIn("Comparison", body)

if __name__ == "__main__":
    unittest.main()
