'''Tests for data source'''
import unittest
from unittest.mock import MagicMock, patch
from records import Record
from ProductionCode.data_source import DataSource

class DataSourceTests(unittest.TestCase):
    '''Class containing tests of Data Soure class'''
    def setUp(self):
        '''create mock data source object to be used'''
        self.patcher = patch("ProductionCode.data_source.records.Database")
        self.mock_database_class = self.patcher.start()

        self.mock_db_instance = MagicMock()
        self.mock_database_class.return_value = self.mock_db_instance

        self.test_source = DataSource()

    def test_sales_state_year(self):
        '''Tests queries for sales for given year and state'''
        self.mock_db_instance.query.return_value.first.return_value = Record(
            ["commercialRevenue","totalPrice"],
            [3059902.25,12.54]
        )

        result = self.test_source.get_sales_state_year("AL", 2025)

        self.assertEqual(result["commercialRevenue"], 3059902.25)
        self.assertEqual(float(result["totalPrice"]), 12.54)


    def test_emissions_state_year(self):
        '''Tests queries for emissions for given year and state'''
        self.mock_db_instance.query.return_value.first.return_value = Record(
            ["generation", "thermalOutput"],
            [27814120731.0, 17095959.0]
        )

        result = self.test_source.get_emissions_state_year("MN", 2024)

        self.assertEqual(result["generation"], 27814120731.0)
        self.assertEqual(result["thermalOutput"], 17095959.0)

    def test_us_23_price(self):
        '''Test loading of US price'''
        self.mock_db_instance.query.return_value.first.return_value = Record(
            ["commercialSales"], [1408108756.04]
        )
        result = self.test_source.get_sales_us_year(2023)
        self.assertEqual(result["commercialSales"], 1408108756.04)

    def test_us_23_emissions(self):
        '''Test loading of US emissions'''
        self.mock_db_instance.query.return_value.first.return_value = Record(
            ["generation"], [2526745161497]
        )
        result = self.test_source.get_emissions_us_year(2023)

        self.assertEqual(result["generation"], 2526745161497)
        self.assertEqual(result["state"], "US")
