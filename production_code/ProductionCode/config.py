"""This module contains litterals that can be used as config"""

DICTIONARY_KEYS_ORDERED = [
    "state",
    "year",
    "generation",
    "thermalOutput",
    "totalFuelConsumption",
    "totalFuelConsumptionGeneration",
    "co2Tons",
    "co2MetricTons",
    "residentialRevenue",
    "residentialSales",
    "residentialCustomers",
    "residentialPrice",
    "commercialRevenue",
    "commercialSales",
    "commercialCustomers",
    "commercialPrice",
    "industrialRevenue",
    "industrialSales",
    "industrialCustomers",
    "industrialPrice",
    "transportationRevenue",
    "transportationSales",
    "transportationCustomers",
    "transportationPrice",
    "totalRevenue",
    "totalSales",
    "totalCustomers",
    "totalPrice"
]
DICTIONARY_KEYS_EMMISIONS_INDEXES = range(2,8)
DICTIONARY_KEYS_PRICES_INDEXES = range(8,len(DICTIONARY_KEYS_ORDERED))

"""*US is considered a State*""" 
STATES_LIST = ["US", "AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA",
"HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO",
"MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA",
"RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"]
