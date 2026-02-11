import sys
import records

import ProductionCode.psql_config as config

class DataSource:
    ''' 
    class which contains functions for retrieving data from the data set 
    '''
    def __init__(self):
        '''Constructor that initiates connection to database'''
        connect = f"postgresql://{config.USER}:{config.PASSWORD}@localhost:5432/{config.DATABASE}"
        self.db = records.Database(connect)

    def get_sales_state_year(self,state,year):
        '''Gets sales info for a state for a year month'''
        results = self.db.query(
            'SELECT State, Year, Sum(residentialRevenue) as "residentialRevenue", Sum(residentialSales) as "residentialSales", Avg(residentialCustomers) as "residentialCustomers", Avg(residentialPrice) as "residentialPrice", Sum(commercialRevenue) as "commercialRevenue", Sum(commercialSales) as "commercialSales", Avg(commercialCustomers) as "commercialCustomers", Avg(commercialPrice) as "commercialPrice", Sum(industrialRevenue) as "industrialRevenue", Sum(industrialSales) as "industrialSales", Avg(industrialCustomers) as "industrialCustomers", Avg(industrialPrice) as "industrialPrice", Sum(transportationRevenue) as "transportationRevenue", Sum(transportationSales) as "transportationSales", Avg(transportationCustomers) as "transportationCustomers", Avg(transportationPrice) as "transportationPrice", Sum(totalRevenue) as "totalRevenue", Sum(totalSales) as "totalSales", Avg(totalCustomers) as "totalCustomers", Avg(totalPrice) as "totalPrice" FROM sales_revenue WHERE state = :state AND year = :year GROUP BY State, Year', 
            state = state, year = year
        )
        row = results.first()
        return row.as_dict()

    def get_sales_us_year(self,year):
        '''Gets sales info for the US for a year''' 
        results = self.db.query(
            'SELECT Year, Sum(residentialRevenue) as "residentialRevenue", Sum(residentialSales) as "residentialSales", Avg(residentialCustomers) as "residentialCustomers", Avg(residentialPrice) as "residentialPrice", Sum(commercialRevenue) as "commercialRevenue", Sum(commercialSales) as "commercialSales", Avg(commercialCustomers) as "commercialCustomers", Avg(commercialPrice) as "commercialPrice", Sum(industrialRevenue) as "industrialRevenue", Sum(industrialSales) as "industrialSales", Avg(industrialCustomers) as "industrialCustomers", Avg(industrialPrice) as "industrialPrice", Sum(transportationRevenue) as "transportationRevenue", Sum(transportationSales) as "transportationSales", Avg(transportationCustomers) as "transportationCustomers", Avg(transportationPrice) as "transportationPrice", Sum(totalRevenue) as "totalRevenue", Sum(totalSales) as "totalSales", Avg(totalCustomers) as "totalCustomers", Avg(totalPrice) as "totalPrice" FROM sales_revenue WHERE year = :year GROUP BY year', 
            year = year
        )
        row = results.first()
        results = row.as_dict()
        results["state"] = "US"
        return results

    def get_emissions_state_year(self,state, year):
        '''Gets emissions data for a state for a year'''
        # Future group by fuelGroup, add fuelGroup to SELECT and add GROUP BY fuelGroup 
        results = self.db.query(
            'SELECT State, Year, SUM(generation) as "generation", SUM(usefullthermaloutput) as "thermalOutput", SUM(totalfuelconsumption) as "totalFuelConsumption", SUM(fuelconsumptionelectricgeneration) as "totalFuelConsumptionGeneration", SUM(fuelconsumptionusefulthermaloutput) as "fuelConsumptionThermalOutput", SUM(quantityoffuelconsumed) as "quantityOfFuelConsumed", SUM(tonsco2emissions) as "co2Tons", SUM(metrictonnesco2emissions) as "co2MetricTons" FROM emissions WHERE state = :state AND year = :year GROUP BY State, Year', 
            state = state, year = year
        )
        row = results.first()
        return row.as_dict()

    def get_emissions_us_year(self, year):
        '''Gets emissions data for the US for a year'''
        # Future group by fuelGroup, add fuelGroup to SELECT and add GROUP BY fuelGroup 
        results = self.db.query(
            'SELECT Year, SUM(generation) as "generation", SUM(usefullthermaloutput) as "thermalOutput", SUM(totalfuelconsumption) as "totalFuelConsumption", SUM(fuelconsumptionelectricgeneration) as "totalFuelConsumptionGeneration", SUM(fuelconsumptionusefulthermaloutput) as "fuelConsumptionThermalOutput", SUM(quantityoffuelconsumed) as "quantityOfFuelConsumed", SUM(tonsco2emissions) as "co2Tons", SUM(metrictonnesco2emissions) as "co2MetricTons" FROM emissions WHERE year = :year GROUP BY year', 
            year = year
        )
        row = results.first()
        results = row.as_dict()
        results["state"] = "US"
        return results

    def get_states_data(self, states, year):
        '''Gets data for states which is passed in as array of state codes'''
        results = []
        for state in states:
            sales = self.get_sales_state_year(state, year)
            emissions = self.get_emissions_state_year(state,year)
            state_result = emissions | sales
            results.append(state_result)
        if len(results) == 1:
            return results[0] 
        return results

    def get_us_year_data(self, year):
        sales = self.get_sales_us_year(year)
        emissions = self.get_emissions_us_year(year)
        us_result = emissions | sales
        return us_result
    
def main():
    ds = DataSource

if __name__ == '__main__':
    main()