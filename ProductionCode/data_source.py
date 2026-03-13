'''
File contains DataSource Class for data base queries
'''
import records

import ProductionCode.psql_config as config
from ProductionCode.config import DICTIONARY_KEYS_ORDERED, DICTIONARY_KEYS_EMMISIONS_INDEXES
from ProductionCode.config import DICTIONARY_KEYS_PRICES_INDEXES
from ProductionCode.config import AVAILABLE_YEARS
from ProductionCode.config import SQL_ALIASES
US_CODE = "US"
class DataSource:
    ''' 
    class which contains functions for retrieving data from the data set 
    '''

    instance = None
    def __new__(cls):
        '''Make DataSource a singleton'''
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        '''Constructor that initiates connection to database'''
        connect = f"postgresql://{config.USER}:{config.PASSWORD}@localhost:5432/{config.DATABASE}"
        self.db = records.Database(connect)

    def get_sales_state_year(self,state,year) -> dict:
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
        return row.as_dict() if row else {}

    def get_sales_us_year(self,year) -> dict:
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
        us_results = results.first().as_dict()
        us_results["state"] = US_CODE
        return us_results if us_results else {}

    def get_emissions_state_year(self,state, year) -> dict:
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
        return row.as_dict() if row else {}

    def get_emissions_us_year(self, year) -> dict:
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
        us_results = results.first().as_dict()
        us_results["state"] = US_CODE
        return us_results if us_results else {}

    def get_states_data(self, states, year) -> list:
        '''
        Gets data for states which is passed in as array of state codes
        param states list: list of string state codes to get data for
        param year int: year to get data for

        return results list: list of dictionaries, dictionaries contain 
        data for each state in states
        '''
        results = []
        for state in states:
            if state == US_CODE:
                results.append(self.get_us_year_data(year))
            else:
                sales = self.get_sales_state_year(state, year)
                emissions = self.get_emissions_state_year(state,year)
                state_result = emissions | sales
                results.append(state_result)
        return results

    def get_comparison(self, states, year) -> list:
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

    def get_us_year_data(self, year) -> dict:
        '''
        Get US emissions and price data
        param year int: year to get data for
        return us_result dict: dictionary containing emissions and price data for us for year
        '''
        sales = self.get_sales_us_year(year)
        emissions = self.get_emissions_us_year(year)
        us_result = {'state': US_CODE} | emissions | sales
        return us_result

    def get_graphable_data(self, state, graph_type) -> list:
        '''
        Gets data for a certain state over all available years
        param state str: two letter state code of state data to get
        param graph_type: type of graph to get data for. Must be in config.DICTIONARY_KEYS_ORDERED
        return data: list of data, 
            [0] = state code, 
            [1] = graph title, 
            [2, 3, ...] = data
        '''
        
        if state == US_CODE:
            return self.get_us_graphable_data(graph_type)

        try:
            index = DICTIONARY_KEYS_ORDERED.index(graph_type)
            sql_col = SQL_ALIASES[index][1]
        except:
            raise KeyError('graph type not present')

        #TODO change graph_type to a nice title?
        data = [state, graph_type]
        if index in DICTIONARY_KEYS_EMMISIONS_INDEXES:
            table = 'emissions'
        elif index in DICTIONARY_KEYS_PRICES_INDEXES:
            table = 'sales_revenue'
        else:
            raise IndexError('data in graph_type is not graphable')

        query_result = self.db.query(f"""
            SELECT year, {sql_col} FROM {table} 
            WHERE state = :state 
            GROUP BY state, year
            ORDER BY year ASC
            """,
            state=state
        )

        year_iterator = AVAILABLE_YEARS[0]
        for row in query_result:
            if row[0] == year_iterator:
                data.append(row[1])
            else:
                data.append(0)
            year_iterator -= 1

        return data   

    def get_us_graphable_data(self, graph_type) -> list:
        '''
        Gets data for the US over all available years
        param graph_type: type of graph to get data for. Must be in config.DICTIONARY_KEYS_ORDERED
        return data: list of data, 
            [0] = state code - set to US_CODE, 
            [1] = graph title, 
            [2, 3, ...] = data
        '''
        try:
            index = DICTIONARY_KEYS_ORDERED.index(graph_type)
            sql_col = SQL_ALIASES[index][1]
        except:
            raise KeyError('graph type not present')

        #TODO change graph_type to a nice title?
        data = [US_CODE, graph_type]
        if index in DICTIONARY_KEYS_EMMISIONS_INDEXES:
            table = 'emissions'
        elif index in DICTIONARY_KEYS_PRICES_INDEXES:
            table = 'sales_revenue'
        else:
            raise IndexError('data in graph_type is not graphable')

        query_result = self.db.query(f"""
            SELECT year, {sql_col} FROM {table}
            GROUP BY year
            ORDER BY year DESC
            """,
        )

        year_iterator = AVAILABLE_YEARS[0]
        for row in query_result:
            if row[0] == year_iterator:
                data.append(row[1])
            else:
                data.append(0)
            year_iterator -= 1

        return data
