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
