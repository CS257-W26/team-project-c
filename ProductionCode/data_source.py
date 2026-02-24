'''
File contains DataSource Class for data base queries
'''
import records

import ProductionCode.psql_config as config
from ProductionCode.config import DICTIONARY_KEYS_ORDERED

class DataSource:
    ''' 
    class which contains functions for retrieving data from the data set 
    '''
    def __init__(self):
        '''Constructor that initiates connection to database'''
        connect = f"postgresql://{config.USER}:{config.PASSWORD}@localhost:5432/{config.DATABASE}"
        self.db = records.Database(connect)

    def get_sales_state_year(self,state,year):
        '''
        Gets sales info for a state for a year month
        param state string: state code the data should be retrieved for
        param year int: year of data to retrieve

        return dict: returns dictionary containing the queried data
        '''
        results = self.db.query(
            'SELECT State, Year, Sum(residentialRevenue) as "residentialRevenue", \
            Sum(residentialSales) as "residentialSales", \
            Round(Avg(residentialCustomers)::numeric, 2) as "residentialCustomers", \
            Round(Avg(residentialPrice)::numeric, 2) as "residentialPrice", \
            Sum(commercialRevenue) as "commercialRevenue", \
            Sum(commercialSales) as "commercialSales", \
            Round(Avg(commercialCustomers)::numeric, 2) as "commercialCustomers", \
            Round(Avg(commercialPrice)::numeric, 2) as "commercialPrice", \
            Sum(industrialRevenue) as "industrialRevenue", \
            Sum(industrialSales) as "industrialSales", \
            Round(Avg(industrialCustomers)::numeric, 2) as "industrialCustomers", \
            Round(Avg(industrialPrice)::numeric, 2) as "industrialPrice", \
            Sum(transportationRevenue) as "transportationRevenue", \
            Sum(transportationSales) as "transportationSales", \
            Round(Avg(transportationCustomers)::numeric, 2) as "transportationCustomers", \
            Round(Avg(transportationPrice)::numeric, 2) as "transportationPrice", \
            Sum(totalRevenue) as "totalRevenue", \
            Sum(totalSales) as "totalSales", \
            Round(Avg(totalCustomers)::numeric, 2) as "totalCustomers", \
            Round(Avg(totalPrice)::numeric, 2) as "totalPrice" \
            FROM sales_revenue WHERE state = :state AND year = :year GROUP BY State, Year',
            state = state, year = year
        )
        row = results.first()
        return row.as_dict()
 
    def get_sales_us_year(self,year):
        '''
        Gets sales info for the US for a year
        param year int: year of data to retrieve for US

        return dict: returns dictionary containing the queried data
        ''' 
        results = self.db.query(
            'SELECT Year, Sum(residentialRevenue) as "residentialRevenue", \
            Sum(residentialSales) as "residentialSales", \
            Round(Avg(residentialCustomers)::numeric, 2) as "residentialCustomers", \
            Round(Avg(residentialPrice)::numeric, 2) as "residentialPrice", \
            Sum(commercialRevenue) as "commercialRevenue", \
            Sum(commercialSales) as "commercialSales", \
            Round(Avg(commercialCustomers)::numeric, 2) as "commercialCustomers", \
            Round(Avg(commercialPrice)::numeric, 2) as "commercialPrice", \
            Sum(industrialRevenue) as "industrialRevenue", \
            Sum(industrialSales) as "industrialSales", \
            Round(Avg(industrialCustomers)::numeric, 2) as "industrialCustomers", \
            Round(Avg(industrialPrice)::numeric, 2) as "industrialPrice", \
            Sum(transportationRevenue) as "transportationRevenue", \
            Sum(transportationSales) as "transportationSales", \
            Round(Avg(transportationCustomers)::numeric, 2) as "transportationCustomers", \
            Round(Avg(transportationPrice)::numeric, 2) as "transportationPrice", \
            Sum(totalRevenue) as "totalRevenue", \
            Sum(totalSales) as "totalSales", \
            Round(Avg(totalCustomers)::numeric, 2) as "totalCustomers", \
            Round(Avg(totalPrice)::numeric, 2) as "totalPrice" \
            FROM sales_revenue WHERE year = :year GROUP BY year',
            year = year
        )
        row = results.first()
        results = row.as_dict()
        results["state"] = "US"
        return results

    def get_emissions_state_year(self,state, year):
        '''
        Gets emissions data for a state for a year
        param state string: state code the data should be retrieved for
        param year int: year of data to retrieve

        return dict: returns dictionary containing the queried data
        '''
        # Future group by fuelGroup, add fuelGroup to SELECT and add GROUP BY fuelGroup
        results = self.db.query(
            'SELECT State, Year, SUM(generation) as "generation", \
            SUM(usefullthermaloutput) as "thermalOutput", \
            SUM(totalfuelconsumption) as "totalFuelConsumption", \
            SUM(fuelconsumptionelectricgeneration) as "totalFuelConsumptionGeneration", \
            SUM(fuelconsumptionusefulthermaloutput) as "fuelConsumptionThermalOutput", \
            SUM(quantityoffuelconsumed) as "quantityOfFuelConsumed", \
            SUM(tonsco2emissions) as "co2Tons", \
            SUM(metrictonnesco2emissions) as "co2MetricTons" \
            FROM emissions WHERE state = :state AND year = :year GROUP BY State, Year',
            state = state, year = year
        )
        row = results.first()
        return row.as_dict()

    def get_emissions_us_year(self, year):
        '''
        Gets emissions data for the US for a year
        param year int: year of data to retrieve for US

        return dict: returns dictionary containing the queried data
        '''
        # Future group by fuelGroup, add fuelGroup to SELECT and add GROUP BY fuelGroup
        results = self.db.query(
            'SELECT Year, SUM(generation) as "generation", \
            SUM(usefullthermaloutput) as "thermalOutput", \
            SUM(totalfuelconsumption) as "totalFuelConsumption", \
            SUM(fuelconsumptionelectricgeneration) as "totalFuelConsumptionGeneration", \
            SUM(fuelconsumptionusefulthermaloutput) as "fuelConsumptionThermalOutput", \
            SUM(quantityoffuelconsumed) as "quantityOfFuelConsumed", \
            SUM(tonsco2emissions) as "co2Tons", \
            SUM(metrictonnesco2emissions) as "co2MetricTons" \
            FROM emissions WHERE year = :year GROUP BY year',
            year = year
        )
        row = results.first()
        results = row.as_dict()
        results["state"] = "US"
        return results

    def get_states_data(self, states, year):
        '''
        Gets data for states which is passed in as array of state codes
        param states list: list of string state codes to get data for
        param year int: year to get data for

        return results list: list of dictionaries, dictionaries contain 
        data for each state in states
        '''
        results = []
        for state in states:
            sales = self.get_sales_state_year(state, year)
            emissions = self.get_emissions_state_year(state,year)
            state_result = emissions | sales
            results.append(state_result)
        return results

    def get_comparison(self, states, year):
        '''
        gets the data for the two states and then adds a third entry that computes the net 
        + or - between them
        param states list: list of string state codes to get data for
        param year int: year to get data for

        return data list: list containing the "comparison" data
        '''
        data = self.get_states_data(states, year)
        comparison = {'state': 'comparison'}
        for key in DICTIONARY_KEYS_ORDERED[2:]:
            if data[0].get(key) is None or data[1].get(key) is None:
                continue
            comparison[key] = data[1].get(key) - data[0].get(key)
        data.append(comparison)
        return data

    def get_us_year_data(self, year):
        '''
        Get US emissions and price data
        param year int: year to get data for
        return us_result dict: dictionary containing emissions and price data for us for year
        '''
        sales = self.get_sales_us_year(year)
        emissions = self.get_emissions_us_year(year)
        us_result = emissions | sales
        return us_result
