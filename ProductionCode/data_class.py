'''Containts data class for loading in data'''
import csv
from ProductionCode.data_processing import to_num_or_zero, filter_entry
class Data:
    '''
    Class which acts as a local database. 
    - loads all the data into one dictionary,
    - returns data by get_data function #TODO
    data_dict:
    each key in dictionary will be StateYear ie "MN2024"
    access an entry with data.data_dict["MN2024"]["generation"] #TODO use functions
    to add a dictionary to table: data.data_dict["MN2024"] #TODO read only class?
    '''
    EMISSIONS_GENERATION_FILE = "Data/state_year_power_summary.csv"
    REVENUE_FILE = "Data/sales_revenue.csv"

    def __init__(self):
        self.data_dict = {}

    def average_customers_prices(self):
        '''
        Docstring for average_customers_prices
        sets the values for customer and prices to the averages 
        :param self: Description
        :return: Description
        :rtype: type[dict]
        '''
        customer_fields = ["residentialCustomers", "commercialCustomers",
                  "industrialCustomers", "transportationCustomers", "totalCustomers"]
        price_fields = ["residentialPrice","commercialPrice","industrialPrice",
                        "transportationPrice","totalPrice"]
        for key in self.data_dict.keys():
            num_months = 12
            if self.data_dict[key]["year"] == 2025:
                num_months = 10
            for customer, price in zip(customer_fields, price_fields):
                self.data_dict[key][customer] = self.data_dict[key][customer] / num_months
                self.data_dict[key][price] = round(self.data_dict[key][price]/num_months, 2)
                if self.data_dict[key]["state"] == "US":
                    self.data_dict[key][customer] *= 51
                    self.data_dict[key][price] /= 51

    def load_price_row(self, row):
        '''
        Docstring for load_price_row
        
        :param self: Description
        :param row: row from csv file to be reader, form of list
        :return: Description
        :rtype: type[dict]
        '''
        state_year_key = row[2] + str(row[0])
        if state_year_key not in self.data_dict:
            self.data_dict[state_year_key] = {}
            self.data_dict[state_year_key]["state"] = row[2]
            self.data_dict[state_year_key]["year"] = int(row[0])
        field_names = ["Revenue", "Sales", "Customers", "Price"]
        sales_types = {
            "residential":  (4, 5, 6, 7),
            "commercial":   (8, 9, 10, 11),
            "industrial":   (12, 13, 14, 15),
            "transportation": (16, 17, 18, 19),
            "total":        (20, 21, 22, 23),
        }

        empty_price_count = 0
        for sale_type, idxs in sales_types.items():
            for field_name, idx in zip(field_names, idxs):
                state_key = sale_type + field_name

                if field_name == "Price" and to_num_or_zero(row[idx]) == 0:
                    empty_price_count += 1

                self.data_dict[state_year_key][state_key] = (
                    self.data_dict[state_year_key].get(state_key, 0)
                    + to_num_or_zero(row[idx])
                )

    def load_us_price_data(self):
        '''Loads us price data'''
        for year in range(2013,2026):
            self.load_us_price_data_for_year(year)


    def load_us_price_data_for_year(self,year):
        '''
        Docstring for load_us_price_data
        adds data for US for year to self.data_dict
        :param self: Description
        :param year: year for us data
        :rtype: type[dict]
        '''
        us_year_key = "US" + str(year)
        if us_year_key not in self.data_dict:
            self.data_dict[us_year_key] = {}
            self.data_dict[us_year_key]["state"] = "US"
            self.data_dict[us_year_key]["year"] =int(year)
        for key in self.data_dict.keys():
            if self.data_dict[key]["year"] != year or self.data_dict[key]["state"] == "US":
                continue
            #fix This will all be replaced with like a mapping but not rn 
            self.data_dict[us_year_key]["residentialRevenue"] = self.data_dict[us_year_key].get("residentialRevenue", 0) + self.data_dict[key]["residentialRevenue"]
            self.data_dict[us_year_key]["residentialSales"] = self.data_dict[us_year_key].get("residentialSales", 0) + self.data_dict[key]["residentialSales"]
            self.data_dict[us_year_key]["residentialCustomers"] = self.data_dict[us_year_key].get("residentialCustomers", 0) + self.data_dict[key]["residentialCustomers"]
            self.data_dict[us_year_key]["residentialPrice"] = self.data_dict[us_year_key].get("residentialPrice", 0) + self.data_dict[key]["residentialPrice"]
            self.data_dict[us_year_key]["commercialRevenue"] = self.data_dict[us_year_key].get("commercialRevenue", 0) + self.data_dict[key]["commercialRevenue"]
            self.data_dict[us_year_key]["commercialSales"] = self.data_dict[us_year_key].get("commercialSales", 0) + self.data_dict[key]["commercialSales"]
            self.data_dict[us_year_key]["commercialCustomers"] = self.data_dict[us_year_key].get("commercialCustomers", 0) + self.data_dict[key]["commercialCustomers"]
            self.data_dict[us_year_key]["commercialPrice"] = self.data_dict[us_year_key].get("commercialPrice", 0) + self.data_dict[key]["commercialPrice"]
            self.data_dict[us_year_key]["industrialRevenue"] = self.data_dict[us_year_key].get("industrialRevenue", 0) + self.data_dict[key]["industrialRevenue"]
            self.data_dict[us_year_key]["industrialSales"] = self.data_dict[us_year_key].get("industrialSales", 0) + self.data_dict[key]["industrialSales"]
            self.data_dict[us_year_key]["industrialCustomers"] = self.data_dict[us_year_key].get("industrialCustomers", 0) + self.data_dict[key]["industrialCustomers"]
            self.data_dict[us_year_key]["industrialPrice"] = self.data_dict[us_year_key].get("industrialPrice", 0) + self.data_dict[key]["industrialPrice"]
            self.data_dict[us_year_key]["transportationRevenue"] = self.data_dict[us_year_key].get("transportationRevenue", 0) + self.data_dict[key]["transportationRevenue"]
            self.data_dict[us_year_key]["transportationSales"] = self.data_dict[us_year_key].get("transportationSales", 0) + self.data_dict[key]["transportationSales"]
            self.data_dict[us_year_key]["transportationCustomers"] = self.data_dict[us_year_key].get("transportationCustomers", 0) + self.data_dict[key]["transportationCustomers"]
            self.data_dict[us_year_key]["transportationPrice"] = self.data_dict[us_year_key].get("transportationPrice", 0) + self.data_dict[key]["transportationPrice"]
            self.data_dict[us_year_key]["totalRevenue"] = self.data_dict[us_year_key].get("totalRevenue", 0) + self.data_dict[key]["totalRevenue"]
            self.data_dict[us_year_key]["totalSales"] = self.data_dict[us_year_key].get("totalSales", 0) + self.data_dict[key]["totalSales"]
            self.data_dict[us_year_key]["totalCustomers"] = self.data_dict[us_year_key].get("totalCustomers", 0) + self.data_dict[key]["totalCustomers"]
            self.data_dict[us_year_key]["totalPrice"] = self.data_dict[us_year_key].get("totalPrice", 0) + self.data_dict[key]["totalPrice"]

    def load_emission_data(self):
        '''Loads emission data for all years and states + US years'''
        with open(self.EMISSIONS_GENERATION_FILE, mode='r', encoding="utf-8") as emission_file:
            reader = csv.DictReader(emission_file)
            for row in reader:
                key = row.get("State") + str(row.get("Year"))
                self.data_dict[key]["generation"] = to_num_or_zero(row.get("Generation (kWh)"))
                self.data_dict[key]["thermalOutput"] = to_num_or_zero(row.get("Useful Thermal Output (MMBtu)"))
                self.data_dict[key]["totalFuelConsumption"] = to_num_or_zero(row.get("Total Fuel Consumption (MMBtu)"))
                self.data_dict[key]["totalFuelConsumptionGeneration"] = to_num_or_zero(row.get("Fuel Consumption for Electric Generation (MMBtu)"))
                self.data_dict[key]["co2Tons"] = to_num_or_zero(row.get("Tons of CO2 Emissions"))
                self.data_dict[key]["co2MetricTons"] = to_num_or_zero(row.get("Metric Tonnes of CO2 Emissions"))

                us_key = "US" + str(row.get("Year"))
                self.data_dict[us_key]["generation"] = self.data_dict[us_key].get("generation",0) + to_num_or_zero(row.get("Generation (kWh)"))
                self.data_dict[us_key]["thermalOutput"] = self.data_dict[us_key].get("thermalOutput",0) + to_num_or_zero(row.get("Useful Thermal Output (MMBtu)"))
                self.data_dict[us_key]["totalFuelConsumption"] = self.data_dict[us_key].get("totalFuelConsumption",0) + to_num_or_zero(row.get("Total Fuel Consumption (MMBtu)"))
                self.data_dict[us_key]["totalFuelConsumptionGeneration"] = self.data_dict[us_key].get("totalFuelConsumptionGeneration",0) + to_num_or_zero(row.get("Fuel Consumption for Electric Generation (MMBtu)"))
                self.data_dict[us_key]["co2Tons"] = self.data_dict[us_key].get("co2Tons",0) + to_num_or_zero(row.get("Tons of CO2 Emissions"))
                self.data_dict[us_key]["co2MetricTons"] = self.data_dict[us_key].get("co2MetricTons",0) + to_num_or_zero(row.get("Metric Tonnes of CO2 Emissions"))

    def load_data(self):
        '''
        Docstring for load_data
        Loads in all the data for each state and year - both emissions and prices
        :param self: Description
        :return: Description
        :rtype: type[dict]
        '''
        #load in price data
        with open(self.REVENUE_FILE, mode='r', newline='', encoding="utf-8") as price_file:
            for _ in range(3):
                next(price_file)
            reader = csv.reader(price_file)
            for row in reader:
                self.load_price_row(row)
        self.load_us_price_data()
        self.average_customers_prices()
        self.load_emission_data()

    def get_data(self, states, flags, year):
        '''
        Returns a list of dicts that contain the data asked by states and flags
        :param self: Description
        :param states: list of two letter state codes (uppercase) to get data for
        :param flags: list of bools 
        :param year: year to get data for (string or int)
        :return: state data
        :rtype: list of dicts
        '''
        return_list = []
        for state in states:
            key = state + str(year)
            entry = self.data_dict.get(key)
            if entry is None:
                return_list.append({'state': state, 'year': year})
            else:
                entry = filter_entry(entry, flags)
                return_list.append(entry)
        return return_list
