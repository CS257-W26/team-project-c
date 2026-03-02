'''Full stack tests'''
import unittest
from unittest.mock import patch, MagicMock
from records import Record


class TestFullStack(unittest.TestCase):
    '''Full Stack tests'''

    def setUp(self):
        # Patch DataSource where core looks it up
        self.patcher = patch("ProductionCode.core.DataSource")
        self.mock_class = self.patcher.start()
        self.addCleanup(self.patcher.stop)

        # Instance returned when DataSource() is called
        self.mock_db = self.mock_class.return_value

        import flask_app
        self.client = flask_app.app.test_client()

    def test_us_data(self):
        '''tests that getting us data works'''

        self.mock_db.get_us_year_data.return_value = {
            "state": "US",
            "year": 2021,
            "commercialRevenue": 3059902.25,
            "totalPrice": 12.54
        }

        response = self.client.get('/us?year=2021', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        body = response.get_data(as_text=True)

        self.assertIn("3,059,902.25", body)

    def test_single_state(self):
        """tests that single state returns valid input"""

        self.mock_db.get_states_data.return_value = [{
            "state": "MN",
            "year": 2020,
            "commercialRevenue": 3059902.25,
            "totalPrice": 12.54
        }]

        response = self.client.get('/bystate/MN/2020/', follow_redirects=True)

        body = response.get_data(as_text=True)

        self.assertIn("MN", body)
        self.assertIn("12.54", body)

class TestFullStackComparison(unittest.TestCase):
    '''Full stack comparison tests'''

    def setUp(self):
        self.patcher = patch("ProductionCode.core.DataSource")
        self.mock_class = self.patcher.start()
        self.addCleanup(self.patcher.stop)

        self.mock_db = self.mock_class.return_value

        self.mock_db.get_comparison.return_value = [
            {"state": "IA", "year": 2015, "totalSales": 100},
            {"state": "FL", "year": 2015, "totalSales": 200},
            {"state": "comparison", "totalSales": 100}
        ]

        import flask_app
        self.client = flask_app.app.test_client()

    def test_multi_state_comparison(self):
        """tests two state comparison"""

        response = self.client.get('/compare/IAFL/2015/', follow_redirects=True)

        body = response.get_data(as_text=True)

        self.assertIn("IA", body)
        self.assertIn("FL", body)
        self.assertIn("comparison", body)


if __name__ == "__main__":
    unittest.main()