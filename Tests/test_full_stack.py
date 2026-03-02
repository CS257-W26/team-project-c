'''Tests for core'''
import unittest
from unittest.mock import patch, MagicMock
from records import Record


class TestFullStack(unittest.TestCase):
    '''Full Stack tests'''

    def setUp(self):
        '''Patches Datasource'''
        self.mock_db_instance = MagicMock()
        def mock_init(instance):
            instance.db = self.mock_db_instance

        self.patcher = patch("ProductionCode.data_source.DataSource.__init__", mock_init)
        self.mock_database_class = self.patcher.start()
        self.addCleanup(self.patcher.stop)
        import flask_app as app
        app.core.db.db = self.mock_db_instance
        self.client = app.app.test_client()

    def test_us_data(self):
        '''tests that getting us data works'''
        self.mock_db_instance.query.return_value.first.return_value = Record(
            ['state', 'year', 'commercialRevenue','totalPrice'],
            ['US', '2021', 3059902.25,12.54]
        )

        response = self.client.get('/us?year=2021', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        body = response.get_data(as_text=True)
        self.assertIn("3,059,902.25", body)

    def test_single_state(self):
        """tests that single state returns valid input"""
        self.mock_db_instance.query.return_value.first.return_value = Record(
            ['state', 'year', 'commercialRevenue','totalPrice'],
            ['MN', '2020', 3059902.25,12.54]
        )
        response = self.client.get('/bystate/MN/2020/', follow_redirects=True)
        body = response.get_data(as_text=True)
        self.assertIn("MN", body)
        self.assertIn('12.54', body)


class TestFullStackComparison(unittest.TestCase):
    '''Test for comparison full stack. We have to mock one level higher because this uses two database queries'''
    def setUp(self):
        '''Patch datasource get_states_data  for get_comparison'''
        self.patcher = patch("ProductionCode.core.db")
        self.mock_data = self.patcher.start()
        self.addCleanup(self.patcher.stop)
        import flask_app as app

        self.mock_data.get_states_data.return_value = [
            {"state": "IA", "year": 2015, "totalSales": 100},
            {"state": "FL", "year": 2015, "totalSales": 200},
            {"state": "comparison", "totalSales": 100}
        ]

        self.client = app.app.test_client()

    def test_multi_state_comparison(self):
        """tests two state comparison"""
        response = self.client.get('/compare/IAFL/2015/', follow_redirects=True)
        body = response.get_data(as_text=True)
        self.assertIn("IA", body)
        self.assertIn("FL", body)
        self.assertIn("comparison", body)

if __name__ == "__main__":
    unittest.main()
