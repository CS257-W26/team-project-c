'''Tests for data source'''
import unittest
from unittest.mock import MagicMock, patch, call
from records import Record
from ProductionCode.data_source import DataSource
from ProductionCode.config import AVAILABLE_YEARS

class DataSourceTests(unittest.TestCase):
    '''Class containing tests of Data Soure class'''
    def test_singleton(self):
        '''Test that DataSource is a singleton'''
        d1 = DataSource()
        d2 = DataSource()
        self.assertEqual(d1, d2)

    def setUp(self):
        '''create mock data source object to be used'''
        DataSource.instance = None
        self.patcher = patch("ProductionCode.data_source.records.Database")
        self.mock_database_class = self.patcher.start()

        self.mock_db_instance = MagicMock()
        self.mock_database_class.return_value = self.mock_db_instance

        self.test_source = DataSource()

    def tearDown(self):
        self.patcher.stop()
        DataSource.instance = None

    def test_sales_state_year(self):
        '''Tests queries for sales for given year and state'''
        self.mock_db_instance.query.return_value.first.return_value = Record(
            ["commercialRevenue","totalPrice"],
            [3059902.25,12.54]
        )

        result = self.test_source.get_sales_state_year("AL", 2025)

        self.assertEqual(result["commercialRevenue"], 3059902.25)
        self.assertEqual(float(result["totalPrice"]), 12.54)

    def test_sales_state_year_empty(self):
        '''Returns empty dict when no sales result exists'''
        self.mock_db_instance.query.return_value.first.return_value = None

        result = self.test_source.get_sales_state_year("AL", 2025)

        self.assertEqual(result, {})

    def test_emissions_state_year(self):
        '''Tests queries for emissions for given year and state'''
        self.mock_db_instance.query.return_value.first.return_value = Record(
            ["generation", "thermalOutput"],
            [27814120731.0, 17095959.0]
        )

        result = self.test_source.get_emissions_state_year("MN", 2024)

        self.assertEqual(result["generation"], 27814120731.0)
        self.assertEqual(result["thermalOutput"], 17095959.0)

    def test_emissions_state_year_empty(self):
        '''Returns empty dict when no emissions result exists'''
        self.mock_db_instance.query.return_value.first.return_value = None

        result = self.test_source.get_emissions_state_year("MN", 2024)

        self.assertEqual(result, {})

    def test_us_23_price(self):
        '''Test loading of US price'''
        self.mock_db_instance.query.return_value.first.return_value = Record(
            ["commercialSales"], [1408108756.04]
        )
        result = self.test_source.get_sales_us_year(2023)
        self.assertEqual(result["commercialSales"], 1408108756.04)
        self.assertEqual(result["state"], "US")

    def test_us_23_emissions(self):
        '''Test loading of US emissions'''
        self.mock_db_instance.query.return_value.first.return_value = Record(
            ["generation"], [2526745161497]
        )
        result = self.test_source.get_emissions_us_year(2023)

        self.assertEqual(result["generation"], 2526745161497)
        self.assertEqual(result["state"], "US")

    @patch.object(DataSource, "get_sales_us_year")
    @patch.object(DataSource, "get_emissions_us_year")
    def test_get_us_year_data(self, mock_emissions, mock_sales):
        '''Test loading all US data'''
        mock_sales.return_value = {"residentialRevenue": 123456}
        mock_emissions.return_value = {"generation": 2340924}
        result = self.test_source.get_us_year_data(2024)
        self.assertEqual(result, {"generation":2340924, "residentialRevenue":123456,
        'state': 'US'})
        mock_sales.assert_called_once_with(2024)
        mock_emissions.assert_called_once_with(2024)

    @patch.object(DataSource, "get_sales_state_year")
    @patch.object(DataSource, "get_emissions_state_year")
    @patch.object(DataSource, "get_us_year_data")
    def test_get_states_data(self, mock_us, mock_emissions, mock_sales):
        '''Test loading states data'''
        mock_sales.return_value = {"residentialRevenue":12345}
        mock_emissions.return_value = {"generation":2345}
        mock_us.return_value = {"state": "US", "generation": 23456}

        results = self.test_source.get_states_data(["KS", "US"], 2024)
        self.assertEqual(
            results,
            [
                {"residentialRevenue": 12345, "generation": 2345},
                {"state": "US", "generation": 23456}
            ]
        )

    @patch.object(DataSource, "get_states_data")
    def test_get_comparison(self, mock_states_data):
        '''Tests Making Comparison'''
        mock_states_data.return_value = [
            {"state": "KS", "generation": 100, "residentialRevenue": 50},
            {"state": "MN", "generation": 150, "residentialRevenue": 70},
        ]
        result = self.test_source.get_comparison(["KS", "MN"], 2024)
        mock_states_data.assert_called_once_with(["KS", "MN"], 2024)
        expected = [
            {"state": "KS", "generation": 100, "residentialRevenue": 50},
            {"state": "MN", "generation": 150, "residentialRevenue": 70},
            {"state": "comparison", "generation": 50, "residentialRevenue": 20},
        ]
        self.assertEqual(result, expected)

    @patch.object(DataSource, "get_states_data")
    def test_get_comparison_with_none(self, mock_states_data):
        '''Comparison should skip None values'''
        mock_states_data.return_value = [
            {"state": "KS", "generation": 100, "residentialRevenue": None},
            {"state": "MN", "generation": 150, "residentialRevenue": 70},
        ]

        result = self.test_source.get_comparison(["KS", "MN"], 2024)

        self.assertEqual(result[2]["state"], "comparison")
        self.assertEqual(result[2]["generation"], 50)
        self.assertNotIn("residentialRevenue", result[2])

    def test_get_graphable_data(self):
        '''Gets graphable state emissions data'''
        self.mock_db_instance.query.return_value = [
            Record((AVAILABLE_YEARS[0], 100), ("year", "generation")),
            Record((AVAILABLE_YEARS[1], 90), ("year", "generation"))
        ]

        result = self.test_source.get_graphable_data("AR", "generation")

        self.assertEqual(result[0], "AR")
        self.assertEqual(result[1], "generation")
        self.assertIn(100, result)
        self.assertIn(90, result)

    def test_get_graphable_data_price(self):
        '''Gets graphable state price data'''
        self.mock_db_instance.query.return_value = [
            Record((AVAILABLE_YEARS[0], 15), ("year", "totalPrice")),
            Record((AVAILABLE_YEARS[1], 14), ("year", "totalPrice"))
        ]

        result = self.test_source.get_graphable_data("AR", "totalPrice")

        self.assertEqual(result[0], "AR")
        self.assertEqual(result[1], "totalPrice")

    def test_get_graphable_data_us(self):
        '''US graphable should call US function'''
        with patch.object(
            DataSource,
            "get_us_graphable_data",
            return_value=["US", "generation", 1, 2]
        ) as mock_us:

            result = self.test_source.get_graphable_data("US", "generation")

            self.assertEqual(result, ["US", "generation", 1, 2])
            mock_us.assert_called_once_with("generation")

    def test_get_graphable_data_bad_key(self):
        '''Bad key should raise error'''
        with self.assertRaises(KeyError):
            self.test_source.get_graphable_data("AR", "badKey")

    def test_get_us_graphable_data(self):
        '''Gets graphable US emissions'''
        self.mock_db_instance.query.return_value = [
            Record((AVAILABLE_YEARS[0], 500), ("year", "generation")),
            Record((AVAILABLE_YEARS[1], 400), ("year", "generation"))
        ]

        result = self.test_source.get_us_graphable_data("generation")

        self.assertEqual(result[0], "US")
        self.assertEqual(result[1], "generation")

    def test_get_us_graphable_data_price(self):
        '''Gets graphable US price data'''
        self.mock_db_instance.query.return_value = [
            Record((AVAILABLE_YEARS[0], 12), ("year", "totalPrice")),
            Record((AVAILABLE_YEARS[1], 11), ("year", "totalPrice"))
        ]

        result = self.test_source.get_us_graphable_data("totalPrice")

        self.assertEqual(result[0], "US")
        self.assertEqual(result[1], "totalPrice")

    def test_get_us_graphable_data_bad_key(self):
        '''Bad key should raise error'''
        with self.assertRaises(KeyError):
            self.test_source.get_us_graphable_data("badKey")
