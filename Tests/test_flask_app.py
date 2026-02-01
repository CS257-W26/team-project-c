'''Tests for flask app'''
import unittest
from unittest.mock import patch

import flask_app as app
from ProductionCode.data_class import Data


class TestFlaskApp(unittest.TestCase):
    '''Tests for flask app'''
    def setUp(self):
        '''Loads data and registers blueprint'''
        if "api" not in app.app.blueprints:
            app.app.register_blueprint(app.api, url_prefix="/api")
        self.client = app.app.test_client()

        self.test_data = Data()
        self.test_data.load_data()

        app.data = self.test_data

    def test_homepage(self):
        '''Tests that homepage is good'''
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        body = response.get_data(as_text=True)
        self.assertIn("Welcome to the homepage", body)
        self.assertIn("/api/US2025", body)

    def test_get_year_data_success(self):
        '''tests that getting data works for valid input'''
        response = self.client.get('/api/US2025/',follow_redirects=True)

        #self.assertEqual(response.status_code, 200)
        body = response.get_data(as_text=True)

        # Table output checks (real TableMaker formatting)
        self.assertIn("State", body)
        self.assertIn("US", body)
        self.assertIn("2025", body)
        self.assertIn("1,285,315,546", body)
        self.assertIn("Transportation Price", body)
        self.assertIn("14.08", body)

    def test_get_year_data_key_error_results_in_500(self):
        '''tests that an invalid dictionary key gives 500 error'''
        response = self.client.get('/api/FAKE9999/',follow_redirects=True)
        self.assertEqual(response.status_code, 500)

        body = response.get_data(as_text=True)
        self.assertIn("technical issue", body)

    def test_404_error_handler(self):
        '''tests that invalid route give 404 error'''
        response = self.client.get("/not/a/route",follow_redirects=True)
        self.assertEqual(response.status_code, 404)

        body = response.get_data(as_text=True)
        self.assertIn("wrong format", body)

    def test_load_data_calls_data_load(self):
        '''Tests load data function'''
        with patch.object(app.data, "load_data") as mock_load:
            app.load_data()
            mock_load.assert_called_once()

    def test_make_table_invalid_entry_type(self):
        '''tests make table function doesnt accept invalid'''
        with self.assertRaises(TypeError):
            app.make_table("not a dict")

    def test_make_table_valid_entry(self):
        '''tests make table with valid entry'''
        entry = {"state": "US", "year": 2025}
        table = app.make_table(entry)

        self.assertEqual(len(table.entries), 1)
        self.assertEqual(table.entries[0]["state"], "US")

    def test_get_year_data_renders_html(self):
        '''Tests template rendering'''
        response = self.client.get("/api/US2025/", follow_redirects= True)
        body = response.get_data(as_text=True)

        self.assertIn("<html>", body)
        self.assertIn("<pre>", body)
        self.assertIn("</html>", body)

    def test_get_year_data_with_minimal_entry(self):
        '''Tests empty(ish) table'''
        app.data.data_dict["US2026"] = {
            "state": "US",
            "year": 2026
        }

        response = self.client.get("/api/US2026/")
        self.assertEqual(response.status_code, 200)

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
