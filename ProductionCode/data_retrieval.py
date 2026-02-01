'''
This file contains functions which retrieve the desired data from the datasets 
for the command line functions to access
'''
import csv

EMISSIONS_FILE = "Data/state_year_power_summary.csv"
LATEST_EMISSIONS_YEAR = "2024"

def get_price_data_state(state, year):
    '''
    Docstring for get_price_data_state
    Accesses sales_revenue.xlsx - Monthly-States.csv
    finds rows for 
    :param state: two letter code for the State which we want data for, 
    if state is US then take all month data for year to aggregate
    :param year: the year of data desired
    
    :return : returns a dict with entries for state/year then entries 
    for the residential/commercial etc. for revenue/sales etc.
    If improper state or year value entered should return dict with empty values and 
    state/year entries as the invalid inputs
    '''
    month_data = []
    with open('Data/sales_revenue.csv', mode='r',newline='') as csv_file:
        for _ in range(3): #skip first two lines of csv file to make third row column headers
            next(csv_file)
        reader = csv.reader(csv_file)
        for row in reader:
            if int(row[0]) < year:
                break
            if (row[2] == state and int(row[0]) == year) or (state == "US" and int(row[0]) == year):
                month_data.append(row)
    return fixed_dict_format(aggregate_month_data_sales(month_data), state)
def aggregate_month_data_sales(month_data):
    '''
    Docstring for aggregate_month_data_sales
    Sums the given month data into one dict containing: 
    totals for revenue, sales, etc and the avg for the prices
    
    :param month_data: list of lists containing all the month data for a year for a state
    :return totals: dict of dicts with each category ("residential" etc) having its own dict
    Dict format:
    {Residential: {Revenue: float, Sales: float, Customers: float, PriceAvg: float}, Commercial: {etc}, etc}
    '''
    field_names = ["revenue", "sales", "customers", "priceAvg"]
    fields = {
    "residential":  (4, 5, 6, 7),
    "commercial":   (8, 9, 10, 11),
    "industrial":   (12, 13, 14, 15),
    "transportation": (16, 17, 18, 19),
    "total":        (20, 21, 22, 23),
    }
    totals = {
        name: {
            "revenue": 0,
            "sales": 0,
            "customers": 0,
            "priceAvg": 0
        } for name in fields
    }
    empty_price_count = 0
    for month in month_data:
        for name, idxs in fields.items():
            for i, idx in zip(field_names, idxs):
                if str(i) == "priceAvg" and to_num_or_zero(month[idx]) == 0:
                    empty_price_count += 1
                totals[name][i] += to_num_or_zero(month[idx])
    num_data_months = len(month_data)
    if num_data_months > 0:
        for name in totals:
            if name == "transportation" and num_data_months != empty_price_count:
                totals[name]["priceAvg"] /= (num_data_months - empty_price_count)
            else: totals[name]["priceAvg"] /= num_data_months
            totals[name]["priceAvg"] = round(totals[name]["priceAvg"],2)
            # customer data is averaged across months
            totals[name]["customers"] = int(totals[name]["customers"]/(num_data_months))
    return totals
def to_num_or_zero(entry):
    '''
    Docstring for to_num_or_zero
    converts the entry for the data into a numeric type
    :param entry: the value for a specific cell in data set
    :return : returns the value of the cell as a float
    '''
    if entry is None:
        return 0
    if isinstance(entry, (int, float)):
        value = float(entry)
    elif isinstance(entry, str):
        entry = entry.strip().strip('"')
        if entry == "." or entry == "":
            return 0
        entry = entry.replace(",", "")
        try:
            value = float(entry)
        except ValueError:
            return 0
    else: return 0
    if value.is_integer():
        return int(value)
    else:
        return round(value, 2)
def fixed_dict_format(totals_dict, state):
    '''
    Docstring for fixed_dict_format
    
    :param totals_dict: dictionary from aggregate function whos formating is being fixed
    :param state: the state for which the dictionary is made for
    year is set to 2025 as fixed year for now, only care about most recent data
    '''
    state_dict = {}
    state_dict["state"] = state
    state_dict["year"] = 2025
    #If state is US need to average months across all states
    if state_dict["state"] == "US":
        state_dict["residentialCustomers"] = int(totals_dict["residential"]["customers"]*51)
        state_dict["commercialCustomers"] = int(totals_dict["commercial"]["customers"]*51)
        state_dict["industrialCustomers"] = int(totals_dict["industrial"]["customers"]*51)
        state_dict["transportationCustomers"] = int(totals_dict["transportation"]["customers"]*51)
        state_dict["totalCustomers"] = int(totals_dict["total"]["customers"]*51)
    else:
        state_dict["residentialCustomers"] = totals_dict["residential"]["customers"]
        state_dict["commercialCustomers"] = totals_dict["commercial"]["customers"]
        state_dict["industrialCustomers"] = totals_dict["industrial"]["customers"]
        state_dict["transportationCustomers"] = totals_dict["transportation"]["customers"]
        state_dict["totalCustomers"] = totals_dict["total"]["customers"]
    state_dict["residentialRevenue"] = totals_dict["residential"]["revenue"]
    state_dict["residentialSales"] = totals_dict["residential"]["sales"]
    state_dict["residentialPrice"] = totals_dict["residential"]["priceAvg"]
    state_dict["commercialRevenue"] = totals_dict["commercial"]["revenue"]
    state_dict["commercialSales"] = totals_dict["commercial"]["sales"]
    state_dict["commercialPrice"] = totals_dict["commercial"]["priceAvg"]
    state_dict["industrialRevenue"] = totals_dict["industrial"]["revenue"]
    state_dict["industrialSales"] = totals_dict["industrial"]["sales"]
    state_dict["industrialPrice"] = totals_dict["industrial"]["priceAvg"]
    state_dict["transportationRevenue"] = totals_dict["transportation"]["revenue"]
    state_dict["transportationSales"] = totals_dict["transportation"]["sales"]
    state_dict["transportationPrice"] = totals_dict["transportation"]["priceAvg"]
    state_dict["totalRevenue"] = totals_dict["total"]["revenue"]
    state_dict["totalSales"] = totals_dict["total"]["sales"]
    state_dict["totalPrice"] = totals_dict["total"]["priceAvg"]
    return state_dict

def getEmissionData(state):
    """
    Returns emissions data for one state using the most recent year
    in state_year_power_summary.csv
    """
    year_to_use = LATEST_EMISSIONS_YEAR

    def toNumber(value):
        if value is None:
            return None
        s = str(value).replace(",","").strip()
        if s == "":
            return None
        try:
            return float(s)
        except:
            return None

    if state == "US":
        totals = {
            "generation": 0.0,
            "thermalOutput": 0.0,
            "totalFuelConsumption": 0.0,
            "totalFuelConsumptionGeneration": 0.0,
            "co2Tons": 0.0,
            "co2MetricTons": 0.0
        }
        found_any = False

        with open(EMISSIONS_FILE, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("Year") != year_to_use:
                    continue

                found_any = True
                totals["generation"] += (toNumber(row.get("Generation (kWh)")) or 0.0)
                totals["thermalOutput"] += (toNumber(row.get("Useful Thermal Output (MMBtu)")) or 0.0)
                totals["totalFuelConsumption"] += (toNumber(row.get("Total Fuel Consumption (MMBtu)")) or 0.0)
                totals["totalFuelConsumptionGeneration"] += (toNumber(row.get("Fuel Consumption for Electric Generation (MMBtu)")) or 0.0)
                totals["co2Tons"] += (toNumber(row.get("Tons of CO2 Emissions")) or 0.0)
                totals["co2MetricTons"] += (toNumber(row.get("Metric Tonnes of CO2 Emissions")) or 0.0)

        if not found_any:
            raise KeyError("No emissions data found for US in " + year_to_use)

        return totals

    with open(EMISSIONS_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("State") == state and row.get("Year") == year_to_use:
                return {
                    "generation": toNumber(row.get("Generation (kWh)")),
                    "thermalOutput": toNumber(row.get("Useful Thermal Output (MMBtu)")),
                    "totalFuelConsumption": toNumber(row.get("Total Fuel Consumption (MMBtu)")),
                    "totalFuelConsumptionGeneration": toNumber(row.get("Fuel Consumption for Electric Generation (MMBtu)")),
                    "co2Tons": toNumber(row.get("Tons of CO2 Emissions")),
                    "co2MetricTons": toNumber(row.get("Metric Tonnes of CO2 Emissions"))
                }

    raise KeyError("No emissions data found for " + state + " in " + year_to_use)

def get_data(states, flags):
    """
    Returns an array of dict entries for TableMaker.

    states: list like ["MN","ND"]
    flags: [prices_flag, emission_flag]
    """
    results = []

    if flags[0] and flags[1]:
        year_label = LATEST_EMISSIONS_YEAR + " / 2025"
    elif flags[1]:
        year_label = LATEST_EMISSIONS_YEAR
    elif flags[0]:
        year_label = "2025"
    else:
        year_label = ""

    for state in states:
        entry = {
            "state": state,
            "year": year_label
        }

        if flags[1]:
            emissions = getEmissionData(state)
            entry.update(emissions)
        
        if flags[0]:
            prices = get_price_data(state)
            entry.update(prices)
        
        results.append(entry)

    return results

def get_price_data(state):
    '''
    Docstring for getPriceData
    
    :param state: two letter state code
    :return dictionary: format is entries for state and year then entries for each column in dataset like residentialReveune or totalPrice
    Example:
    dict["state"] = KS if state param is KS
    dict["residentialRevenue"] = residential revenue for year 2025 in KS, summed values from all months 
    '''
    return get_price_data_state(state, 2025) 


def main():
    ''' 
    Main 
    '''
    US25 = get_price_data_state("US", 2025)
    KY25 = get_price_data_state("KY", 2025)
    #print(US25["transportationPrice"])
    print(US25["commercialCustomers"])
    print(KY25["commercialCustomers"])
    print(KY25["totalCustomers"])

if __name__ == "__main__":
    main()
