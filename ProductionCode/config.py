"""This module contains litterals that can be used as config
when adding new fields"""

#*US is considered a State*
AUTOCOMPLETE_OPTIONS = [
    'All-United States US',
    'Alabama AL',
    'Alaska AK',
    'Arizona AZ',
    'Arkansas AR',
    'California CA',
    'Colorado CO',
    'Connecticut CT',
    'Delaware DE',
    'Florida FL',
    'Georgia GA',
    'Hawaii HI',
    'Idaho ID',
    'Illinois IL',
    'Indiana IN',
    'Iowa IA',
    'Kansas KS',
    'Kentucky KY',
    'Louisiana LA',
    'Maine ME',
    'Maryland MD',
    'Massachusetts MA',
    'Michigan MI',
    'Minnesota MN',
    'Mississippi MS',
    'Missouri MO',
    'Montana MT',
    'Nebraska NE',
    'Nevada NV',
    'New Hampshire NH',
    'New Jersey NJ',
    'New Mexico NM',
    'New York NY',
    'North Carolina NC',
    'North Dakota ND',
    'Ohio OH',
    'Oklahoma OK',
    'Oregon OR',
    'Pennsylvania PA',
    'Rhode Island RI',
    'South Carolina SC',
    'South Dakota SD',
    'Tennessee TN',
    'Texas TX',
    'Utah UT',
    'Vermont VT',
    'Virginia VA',
    'Washington WA',
    'West Virginia WV',
    'Wisconsin WI',
    'Wyoming WY'
]

AUTOCOMPLETE_ALLIASES = STATES_LIST = [
    'US', 'AL', 'AK', 'AZ', 'AR', 'CA',
    'CO', 'CT', 'DE', 'FL', 'GA', 'HI',
    'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
    'LA', 'ME', 'MD', 'MA', 'MI', 'MN',
    'MS', 'MO', 'MT', 'NE', 'NV', 'NH',
    'NJ', 'NM', 'NY', 'NC', 'ND', 'OH',
    'OK', 'OR', 'PA', 'RI', 'SC', 'SD',
    'TN', 'TX', 'UT', 'VT', 'VA', 'WA',
    'WV', 'WI', 'WY'
]

AVAILABLE_YEARS = [
    '2024',
    '2023',
    '2022',
    '2021',
    '2020',
    '2019',
    '2018',
    '2017',
    '2016',
    '2015',
    '2014',
    '2013'
]

# (Dict alias, TableMaker alias, sql col alias, General Title)
ALIASES = [
    ("state"                          
        , "state"                                    
        , "State                           "
        , 'State'),
    ("year"                           
        , "year"                                     
        , "Year                            "
        , "Year"),
    ("generation"                     
        , 'SUM(generation) as "generation"'          
        , "Generation                 (kWh)"
        , "Generation (kWh)"),
    ("thermalOutput"                  
        , 'SUM(usefullthermaloutput) as "thermalOutput"'
        , "Useful Thermal Output    (MMBtu)"
        , "Useful Thermal Output (MMBtu)"),
    ("totalFuelConsumption"           
        , 'SUM(totalfuelconsumption) as "totalFuelConsumption"'
        , "Total Fuel Consumption   (MMBtu)"
        , "Total Fuel Consumption (MMBtu)"),
    ("totalFuelConsumptionGeneration" 
        , 'SUM(fuelconsumptionelectricgeneration) as "totalFuelConsumptionGeneration"'
        , "Total Fuel Consumption for      |\nElectric Generation      (MMBtu)"
        , "Total Fuel Consumption for Electric Generation (MMBtu)"),
    ("fuelConsumptionThermalOutput"   
        , 'SUM(fuelconsumptionusefulthermaloutput) as "fuelConsumptionThermalOutput"'
        , "Fuel Consumption for Useful     |\nThermal Output           (MMBtu)"
        , "Fuel Consumption for Useful Thermal Output (MMBtu)"),
    ("quantityOfFuelConsumed"         
        , 'SUM(quantityoffuelconsumed) as "quantityOfFuelConsumed"'
        , "Quanitty of Fuel Units Consumed"
        , "Quanitty of Fuel Units Consumed \
        (but this is wrong and we need to get rid of it from UI)"),
    ("co2Tons"                        
        , 'SUM(tonsco2Emissions) as "co2Tons"'
        , "CO2 Emmissions            (Tons)"
        , "CO2 Emmissions (Tons)"),
    ("co2MetricTons"                  
        , 'SUM(metricTonnesco2Emissions) as "co2MetricTons"'
        , "CO2 Emmissions     (Metric Tons)"
        , "CO2 Emmissions (Metric Tons)"),
    ("residentialRevenue"             
        , 'Sum(residentialRevenue) as "residentialRevenue"'
        , "Residential Revenue        ($1K)"
        , "Residential Revenue ($1K)"),
    ("residentialSales"               
        , 'Sum(residentialSales) as "residentialSales"'
        , "Residential Sales          (MWh)"
        , "Residential Sales (MWh)"),
    ("residentialCustomers"           
        , 'Round(Avg(residentialCustomers)::numeric, 2) as "residentialCustomers"'
        , "Residential Customers           "
        , "Residential Customers"),
    ("residentialPrice"               
        , 'Round(Avg(residentialPrice)::numeric, 2) as "residentialPrice"'
        , "Residential Price    (cents/kWh)"
        , "Residential Price (cents/kWh)"),
    ("commercialRevenue"              
        , 'Sum(commercialRevenue) as "commercialRevenue"'
        , "Commercial Revenue         ($1K)"
        , "Commercial Revenue ($1K)"),
    ("commercialSales"                
        , 'Sum(commercialSales) as "commercialSales"'
        , "Commercial Sales           (MWh)"
        , "Commercial Sales (MWh)"),
    ("commercialCustomers"            
        , 'Round(Avg(commercialCustomers)::numeric, 2) as "commercialCustomers"'
        , "Commercial Customers            "
        , "Commercial Customers"),
    ("commercialPrice"                
        , 'Round(Avg(commercialPrice)::numeric, 2) as "commercialPrice"'
        , "Commercial Price     (cents/kWh)"
        , "Commercial Price (cents/kWh)"),
    ("industrialRevenue"              
        , 'Sum(industrialRevenue) as "industrialRevenue"'
        , "Industrial Revenue         ($1K)"
        , "Industrial Revenue ($1K)"),
    ("industrialSales"                
        , 'Sum(industrialSales) as "industrialSales"'
        , "Industrial Sales           (MWh)"
        , "Industrial Sales (MWh)"),
    ("industrialCustomers"            
        , 'Round(Avg(industrialCustomers)::numeric, 2) as "industrialCustomers"'
        , "Industrial Customers            "
        , "Industrial Customers"),
    ("industrialPrice"                
        , 'Round(Avg(industrialPrice)::numeric, 2) as "industrialPrice"'
        , "Industrial Price     (cents/kWh)"
        , "Industrial Price (cents/kWh)"),
    ("transportationRevenue"          
        , 'Sum(transportationRevenue) as "transportationRevenue"'
        , "Transportation Revenue     ($1K)"
        , "Transportation Revenue ($1K)"),
    ("transportationSales"            
        , 'Sum(transportationSales) as "transportationSales"'
        , "Transportation Sales       (MWh)"
        , "Transportation Sales (MWh)"),
    ("transportationCustomers"        
        , 'Round(Avg(transportationCustomers)::numeric, 2) as "transportationCustomers"'
        , "Transportation Customers        "
        , "Transportation Customers"),
    ("transportationPrice"            
        , 'Round(Avg(transportationPrice)::numeric, 2) as "transportationPrice"'
        , "Transportation Price (cents/kWh)"
        , "Transportation Price (cents/kWh)"),
    ("totalRevenue"                   
        , 'Sum(totalRevenue) as "totalRevenue"'
        , "Total Revenue              ($1K)"
        , "Total Revenue ($1K)"),
    ("totalSales"                     
        , 'Sum(totalSales) as "totalSales"'
        , "Total Sales                (MWh)"
        , "Total Sales (MWh)"),
    ("totalCustomers"                 
        , 'Round(Avg(totalCustomers)::numeric, 2) as "totalCustomers"'
        , "Total Customers                 "
        , "Total Customers"),
    ("totalPrice"                     
        , 'Round(Avg(totalPrice)::numeric, 2) as "totalPrice"'
        , "Total Price          (cents/kWh)"
        , "Total Price (cents/kWh)")
]

SQL_ALIASES = [(x[0], x[1]) for x in ALIASES]
DISPLAY_ALIASES = [(x[0], x[2]) for x in ALIASES]
#[2:] because the first two, state, year, are ungraphable
TITLE_ALIASES = [(x[0], x[3]) for x in ALIASES][2:]

DICTIONARY_KEYS_ORDERED = [x[0] for x in DISPLAY_ALIASES]
DICTIONARY_KEYS_EMMISIONS_INDEXES = range(2,8)
DICTIONARY_KEYS_PRICES_INDEXES = range(8,len(DICTIONARY_KEYS_ORDERED))
