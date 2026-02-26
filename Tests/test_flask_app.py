'''Tests for flask api'''
import unittest
import importlib
from unittest.mock import patch

with patch("ProductionCode.data_source.records.Database"):
    import flask_app as app
    importlib.reload(app)

class TestFlaskApp(unittest.TestCase):
    '''Tests for flask app'''

    def setUp(self):
        '''Sets up client, patches core'''

        self.client = app.app.test_client()

        self.patcher = patch("flask_app.core")
        self.mock_data = self.patcher.start()
        self.addCleanup(self.patcher.stop)

        self.mock_data.get_us_year_data.return_value = {
            "state": "US",
            "year": 2024,
            "transportationPrice": 13.31
        }

        self.mock_data.get_states_data.return_value = {
            "state": "MN",
            "year": 2015,
            "totalSales": 8029473,
            "residentialPrice": 2.00
        }

        self.mock_data.get_comparison.return_value = [
            {"state": "IA", "year": 2015, "totalSales": 100},
            {"state": "FL", "year": 2015, "totalSales": 200},
            {"state": "comparison", "totalSales": 100}
        ]

    def test_homepage(self):
        '''Tests that homepage is good'''
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        body = response.get_data(as_text=True)
        self.assertIn("Watt Watch USA", body)

    def test_get_us_data(self):
        '''tests that getting us data works'''
        response = self.client.get('/us/2024/',follow_redirects=True)
        response = response.get_data(as_text=True)
        self.assertIn("US", response)
        self.assertIn("2024", response)
        self.assertIn("Transportation Price", response)

    def test_single_state_success(self):
        """tests that single state returns json for valid input"""
        response = self.client.get('/bystate/MN/2015/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response = response.get_data(as_text=True)
        self.assertIn("MN", response)
        self.assertIn("2015", response)
        self.assertin("8029473", response)

    def test_multi_state_comparison(self):
        """tests two state comparison"""
        response = self.client.get('/compare/iafl/2015/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response = response.get_data(as_text=True)
        self.assertIn("IA", response)
        self.assertIn("FL", response)
        self.assertIn("comparison", response)

    def test_404_error_handler(self):
        '''tests that invalid route give 404 error'''
        response = self.client.get("/not/a/route",follow_redirects=True)
        self.assertEqual(response.status_code, 404)

        body = response.get_data(as_text=True)
        self.assertIn("404 Not Found:", body)


if __name__ == "__main__":
    unittest.main()
