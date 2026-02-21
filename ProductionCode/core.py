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
