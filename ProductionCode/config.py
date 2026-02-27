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

DISPLAY_ALIASES = [
    ("state"                          , "State                           "),
    ("year"                           , "Year                            "),
    ("generation"                     , "Generation                 (kWh)"),
    ("thermalOutput"                  , "Useful Thermal Output    (MMBtu)"),
    ("totalFuelConsumption"           , "Total Fuel Consumption   (MMBtu)"),
    ("totalFuelConsumptionGeneration" , "Total Fuel Consumption for      |\n\
Electric Generation      (MMBtu)"),
    ("fuelConsumptionThermalOutput"   , "Fuel Consumption for Useful     |\n\
Thermal Output           (MMBtu)"),
    ("quantityOfFuelConsumed"         , "Quanitty of Fuel Units Consumed "),
    ("co2Tons"                        , "CO2 Emmissions            (Tons)"),
    ("co2MetricTons"                  , "CO2 Emmissions     (Metric Tons)"),
    ("residentialRevenue"             , "Residential Revenue        ($1K)"),
    ("residentialSales"               , "Residential Sales          (MWh)"),
    ("residentialCustomers"           , "Residential Customers           "),
    ("residentialPrice"               , "Residential Price    (cents/kWh)"),
    ("commercialRevenue"              , "Commercial Revenue         ($1K)"),
    ("commercialSales"                , "Commercial Sales           (MWh)"),
    ("commercialCustomers"            , "Commercial Customers            "),
    ("commercialPrice"                , "Commercial Price     (cents/kWh)"),
    ("industrialRevenue"              , "Industrial Revenue         ($1K)"),
    ("industrialSales"                , "Industrial Sales           (MWh)"),
    ("industrialCustomers"            , "Industrial Customers            "),
    ("industrialPrice"                , "Industrial Price     (cents/kWh)"),
    ("transportationRevenue"          , "Transportation Revenue     ($1K)"),
    ("transportationSales"            , "Transportation Sales       (MWh)"),
    ("transportationCustomers"        , "Transportation Customers        "),
    ("transportationPrice"            , "Transportation Price (cents/kWh)"),
    ("totalRevenue"                   , "total Revenue              ($1K)"),
    ("totalSales"                     , "total Sales                (MWh)"),
    ("totalCustomers"                 , "total Customers                 "),
    ("totalPrice"                     , "total Price          (cents/kWh)")
]

DICTIONARY_KEYS_ORDERED = [x[0] for x in DISPLAY_ALIASES]
DICTIONARY_KEYS_EMMISIONS_INDEXES = range(2,8)
DICTIONARY_KEYS_PRICES_INDEXES = range(8,len(DICTIONARY_KEYS_ORDERED))
