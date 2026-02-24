'''This file should contain one (or maybe a few more) functions that return hard-coded data for your Flask app to use.'''

def get_comparison(states, year):
    """returns comparison data at year - currently hard coded"""
    return [
    {
    "state":'WY',
    "year":'2015',
    "generation":'43,858,392,125',
    "thermalOutput": '14,873,309',
    "totalFuelConsumption": '494,822,363',
    "totalFuelConsumptionGeneration": '466,646,092' 
    },
    {
    "state":'CA',
    "year":'2015',
    "generation":'128,827,275,130',
    "thermalOutput": '93,721,618',
    "totalFuelConsumption": '1,070,264,414',
    "totalFuelConsumptionGeneration": '1,000,395,758'
    },
    {
    "state":'comparison',
    "generation":'84,968,883,005',
    "thermalOutput": '78,848,309',
    "totalFuelConsumption": '575,442,051',
    "totalFuelConsumptionGeneration": '533,749,666'
    }
]
def get_us_year_data(year):
    sale_data = {
        "residentialRevenue": 1000, "residentialSales": 200, "residentialCustomers": 50, "residentialPrice": 10.0,
        "commercialRevenue": 1000, "commercialSales": 200, "commercialCustomers": 50, "commercialPrice": 10.0,
        "industrialRevenue": 1000, "industrialSales": 200, "industrialCustomers": 50, "industrialPrice": 10.0,
        "totalRevenue": 1000, "totalSales": 200, "totalCustomers": 50, "totlaPrice": 10.0,
    }
    emission_data = {
        "generation": 1000, "thermalOuput": 5000, "totalFuelConsumption": 100, "totalFuelConsumptionGeneration": 200,
        "fuelConsumptionThermalOutput": 500, "quantityOfFuelConsumed":150, "co2Tons":500, "co2MetricTons":240
    }
    us_result = emission_data | sale_data
    us_result["state"] = "US" 
    us_result["year"] = year
    return us_result

def get_state_year_data(state, year):
    """Return dummy data for a small set of states only."""
    dummy_by_state = {
        "MN": {
            "generation": 1_250_000,
            "thermalOutput": 6_200,
            "totalFuelConsumption": 110_000,
            "totalFuelConsumptionGeneration": 95_000,
            "fuelConsumptionThermalOutput": 21_000,
            "quantityOfFuelConsumed": 12_000,
            "co2Tons": 52_000,
            "co2MetricTons": 47_000,

            "residentialRevenue": 820_000,
            "residentialSales": 155_000,
            "residentialCustomers": 41_000,
            "residentialPrice": 9.7,

            "commercialRevenue": 910_000,
            "commercialSales": 182_000,
            "commercialCustomers": 36_000,
            "commercialPrice": 10.4,

            "industrialRevenue": 690_000,
            "industrialSales": 208_000,
            "industrialCustomers": 16_000,
            "industrialPrice": 9.1,

            "transportationRevenue": 130_000,
            "transportationSales": 44_000,
            "transportationCustomers": 5_500,
            "transportationPrice": 12.2,

            "totalRevenue": 2_550_000,
            "totalSales": 589_000,
            "totalCustomers": 98_500,
            "totalPrice": 10.1,
        },
        "CA": {
            "generation": 3_900_000,
            "thermalOutput": 18_500,
            "totalFuelConsumption": 340_000,
            "totalFuelConsumptionGeneration": 300_000,
            "fuelConsumptionThermalOutput": 75_000,
            "quantityOfFuelConsumed": 41_000,
            "co2Tons": 120_000,
            "co2MetricTons": 109_000,

            "residentialRevenue": 2_600_000,
            "residentialSales": 420_000,
            "residentialCustomers": 120_000,
            "residentialPrice": 12.4,

            "commercialRevenue": 3_150_000,
            "commercialSales": 510_000,
            "commercialCustomers": 90_000,
            "commercialPrice": 13.1,

            "industrialRevenue": 1_850_000,
            "industrialSales": 470_000,
            "industrialCustomers": 35_000,
            "industrialPrice": 10.8,

            "transportationRevenue": 300_000,
            "transportationSales": 80_000,
            "transportationCustomers": 9_000,
            "transportationPrice": 14.0,

            "totalRevenue": 7_900_000,
            "totalSales": 1_480_000,
            "totalCustomers": 254_000,
            "totalPrice": 12.9,
        }
    }

    state = (state or "").upper()

    result = dict(dummy_by_state[state])
    result["state"] = state
    result["year"] = year
    return result
