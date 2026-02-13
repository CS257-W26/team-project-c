'''Tests for data source'''
import unittest
from unittest.mock import patch

from ProductionCode.data_source import DataSource

class DataSourceTests(unittest.TestCase):
    '''Class containing tests of Data Soure class'''
    def setUp(self):
        '''create DataSource object to be used'''
        self.test_source = DataSource()

    @patch.object(DataSource, "get_sales_state_year")
    def test_sales_state_year(self, mock_get_sales_state_year):
        """Tests queries for sales for given year and state"""
        mock_get_sales_state_year.return_value = {
            "commercialRevenue": 3059902.25,
            "totalPrice": 12.54
        }

        test_al_25 = self.test_source.get_sales_state_year("AL", 2025)

        self.assertEqual(test_al_25["commercialRevenue"], 3059902.25)
        self.assertEqual(float(test_al_25["totalPrice"]), 12.54)

        mock_get_sales_state_year.assert_called_once_with("AL", 2025)

    @patch.object(DataSource, "get_emissions_state_year")
    def test_emissions_state_year(self, mock_get_emissions_state_year):
        """Tests queries for emissions for given year and state"""
        mock_get_emissions_state_year.return_value = {
            "generation": 27814120731.0,
            "thermalOutput": 17095959.0
        }

        test_mn_24 = self.test_source.get_emissions_state_year("MN", 2024)

        self.assertEqual(test_mn_24["generation"], 27814120731.0)
        self.assertEqual(test_mn_24["thermalOutput"], 17095959.0)

        mock_get_emissions_state_year.assert_called_once_with("MN", 2024)

    @patch.object(DataSource, "get_sales_us_year")
    def test_us_23_price(self, mock_get_sales_us_year):
        """Test loading of US price"""
        mock_get_sales_us_year.return_value = {
            "commercialSales": 1408108756.0399995
        }

        test_us_23 = self.test_source.get_sales_us_year(2023)

        self.assertEqual(test_us_23["commercialSales"], 1408108756.0399995)
        mock_get_sales_us_year.assert_called_once_with(2023)

    @patch.object(DataSource, "get_emissions_us_year")
    def test_us_23_emissions(self, mock_get_emissions_us_year):
        """Test loading of US emissions"""
        mock_get_emissions_us_year.return_value = {
            "generation": 2526745161497
        }

        test_us_23 = self.test_source.get_emissions_us_year(2023)

        self.assertEqual(test_us_23["generation"], 2526745161497)
        mock_get_emissions_us_year.assert_called_once_with(2023)
