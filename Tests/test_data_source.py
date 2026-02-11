'''Tests for data source'''
import unittest
from ProductionCode.data_source import DataSource

class DataSourceTests(unittest.TestCase):
    '''Class containing tests of Data Soure class'''
    def setUp(self):
        '''create DataSource object to be used'''
        self.test_source = DataSource()
    
    def test_sales_state_year(self):
        '''Tests queries for sales for given year and state'''
        test_al_25 = self.test_source.get_sales_state_year("AL", 2025)
        self.assertEqual(test_al_25["commercialrevenue"], 3059902.25)
        self.assertEqual(test_al_25["totalprice"], 12.538181818181817)

    def test_emissions_state_year(self):
        '''Tests queries for sales for given year and state'''
        test_mn_24 = self.test_source.get_emissions_state_year("MN", 2024)
        self.assertEqual(test_mn_24["generation"], 27814120731.0)
        self.assertEqual(test_mn_24["usefullthermaloutput"], 17095959.0)

    def test_us_23_price(self):
        '''test loading of us price'''
        test_us_23 = self.test_source.get_sales_us_year(2023)
        self.assertEqual(test_us_23["commercialsales"], 1408108756.0399995)

    def test_us_23_emissions(self):
        '''test loading of US emissions'''
        test_us_23 = self.test_source.get_emissions_us_year(2023)
        self.assertEqual(test_us_23["generation"],2526745161497)
