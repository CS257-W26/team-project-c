'''Tests for flask app'''
import unittest

import flask_app as app
from flask_app import python_bug
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

    def test_get_year_data_success(self):
        '''tests that getting data works for valid input'''
        response = self.client.get('/api/us/2025/',follow_redirects=True)

        #self.assertEqual(response.status_code, 200)
        body = response.get_data(as_text=True)

        # Table output checks (real TableMaker formatting)
        self.assertIn("State", body)
        self.assertIn("US", body)
        self.assertIn("2025", body)
        self.assertIn("1,285,315,546", body)
        self.assertIn("Transportation Price", body)
        self.assertIn("14.08", body)

    def test_single_state_fail(self):
        """Test an icorrectly formated path"""
        response = self.client.get('/api/caa/2015/', follow_redirects=True)
        self.assertIn(b'could not be parsed', response.data)

    def test_multi_state_comparison(self):
        """tests two state comparison"""
        response = self.client.get('/api/iafl/2015/compare/', follow_redirects=True)
        self.assertIn(b'+8,029,474', response.data)
        self.assertIn(b'+2', response.data)

    def test_multi_state_comparison_fail(self):
        """Test an icorrectly formated path"""
        response = self.client.get('/api/cann/2015/compare/', follow_redirects=True)
        self.assertIn(b'cann could not be parsed.', response.data)

    def test_python_bug(self):
        """test_500_page output"""
        response = python_bug(Exception())
        self.assertIn(500, response)

    def test_404_error_handler(self):
        '''tests that invalid route give 404 error'''
        response = self.client.get("/not/a/route",follow_redirects=True)
        self.assertEqual(response.status_code, 404)

        body = response.get_data(as_text=True)
        self.assertIn("wrong format", body)

    def test_get_year_data_renders_html(self):
        '''Tests template rendering'''
        response = self.client.get("/api/us/2025/", follow_redirects= True)
        body = response.get_data(as_text=True)

        self.assertIn("<html>", body)
        self.assertIn("<pre>", body)
        self.assertIn("</html>", body)

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
