'''Tests for flask api'''
import unittest
import importlib
from unittest.mock import patch

with patch("ProductionCode.data_source.records.Database"):
    import flask_api as app
    importlib.reload(app)

class TestFlaskApi(unittest.TestCase):
    '''Tests for flask api'''

    def setUp(self):
        '''Registers blueprint, sets up client, patches core'''
        if "api" not in app.app.blueprints:
            app.app.register_blueprint(app.api, url_prefix="/api")

        self.client = app.app.test_client()

        self.patcher = patch("flask_api.core")
        self.mock_data = self.patcher.start()
        self.addCleanup(self.patcher.stop)

        self.mock_data.get_us_year_data.return_value = {
            "state": "US",
            "year": 2024,
            "transportationPrice": 13.31
        }

        self.mock_data.get_states_data.return_value = [{
            "state": "MN",
            "year": 2015,
            "totalSales": 8029473,
            "residentialPrice": 2.00
        }]

        self.mock_data.get_comparison.return_value = [
            {"state": "IA", "year": 2015, "totalSales": 100},
            {"state": "FL", "year": 2015, "totalSales": 200},
            {"state": "comparison", "totalSales": 100}
        ]

    def test_homepage(self):
        '''Tests that homepage is good'''
        response = self.client.get('/api/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        body = response.get_data(as_text=True)
        self.assertIn("Welcome to the homepage", body)

    def test_get_year_data_success(self):
        '''tests that getting data works for valid input'''
        response = self.client.get('/api/allus/2024/',follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertEqual(data["state"], "US")
        self.assertEqual(data["year"], 2024)
        self.assertIn("transportationPrice", data)

        self.mock_data.get_us_year_data.assert_called_once_with(2024)

    def test_single_state_success(self):
        """tests that single state returns json for valid input"""
        response = self.client.get('/api/bystate/MN/2015/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertEqual(data["state"], "MN")
        self.assertEqual(data["year"], 2015)
        self.assertEqual(data["totalSales"], 8029473)

        self.mock_data.get_states_data.assert_called_once_with("MN", 2015)

    def test_single_state_fail(self):
        """Test an icorrectly formated path"""
        response = self.client.get('/api/bystate/caa/2015/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        body = response.get_data(as_text=True)
        self.assertIn("could not be parsed", body)

        self.mock_data.get_states_data.assert_not_called()

    def test_multi_state_comparison(self):
        """tests two state comparison"""
        response = self.client.get('/api/compare/iafl/2015/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertEqual(data[0]["state"], "IA")
        self.assertEqual(data[1]["state"], "FL")
        self.assertEqual(data[2]["state"], "comparison")

        self.mock_data.get_comparison.assert_called_once_with("iafl", 2015)

    def test_404_error_handler(self):
        '''tests that invalid route give 404 error'''
        response = self.client.get("/not/a/route",follow_redirects=True)
        self.assertEqual(response.status_code, 404)

        body = response.get_data(as_text=True)
        self.assertIn("wrong format", body)

    def test_page_not_found_handler_direct(self):
        '''Tests page not found'''
        msg, status = app.page_not_found(Exception())
        self.assertEqual(status, 404)
        self.assertIn("wrong format", msg)


    def test_python_bug_handler_direct(self):
        '''Tests system error'''
        msg, status = app.python_bug(Exception())
        self.assertEqual(status, 500)
        self.assertIn("technical issue", msg)


if __name__ == "__main__":
    unittest.main()
