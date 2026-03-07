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

ALIASES = [
    ("state"                          , "state"                                    , "State                           "),
    ("year"                           , "year"                                     , "Year                            "),
    ("generation"                     , "generation"                               , "Generation                 (kWh)"),
    ("thermalOutput"                  , "usefulthermaloutput"                      , "Useful Thermal Output    (MMBtu)"),
    ("totalFuelConsumption"           , "totalfuelconsumption"                     , "Total Fuel Consumption   (MMBtu)"),
    ("totalFuelConsumptionGeneration" , "fuelconsumptionelectricgeneration"        , "Total Fuel Consumption for      |\nElectric Generation      (MMBtu)"),
    ("fuelConsumptionThermalOutput"   , "fuelconsumptionusefulthermaloutput"       , "Fuel Consumption for Useful     |\nThermal Output           (MMBtu)"),
    ("quantityOfFuelConsumed"         , "quantityfuelconsumed "                    , "Quanitty of Fuel Units Consumed "),
    ("co2Tons"                        , "tonsco2emmissions"                        , "CO2 Emmissions            (Tons)"),
    ("co2MetricTons"                  , "metrictonsco2emmissions"                  , "CO2 Emmissions     (Metric Tons)"),
    ("residentialRevenue"             , "residentialrevenue"                       , "Residential Revenue        ($1K)"),
    ("residentialSales"               , "residentialsales"                         , "Residential Sales          (MWh)"),
    ("residentialCustomers"           , "residentialcustomers"                     , "Residential Customers           "),
    ("residentialPrice"               , "residentialprice"                         , "Residential Price    (cents/kWh)"),
    ("commercialRevenue"              , "commercialrevenue"                        , "Commercial Revenue         ($1K)"),
    ("commercialSales"                , "commercialsales"                          , "Commercial Sales           (MWh)"),
    ("commercialCustomers"            , "commercialcustomers"                      , "Commercial Customers            "),
    ("commercialPrice"                , "commercialprice"                          , "Commercial Price     (cents/kWh)"),
    ("industrialRevenue"              , "industrialrevenue"                        , "Industrial Revenue         ($1K)"),
    ("industrialSales"                , "industrialsales"                          , "Industrial Sales           (MWh)"),
    ("industrialCustomers"            , "industrialcustomers"                      , "Industrial Customers            "),
    ("industrialPrice"                , "industrialprice"                          , "Industrial Price     (cents/kWh)"),
    ("transportationRevenue"          , "transportationrevenue"                    , "Transportation Revenue     ($1K)"),
    ("transportationSales"            , "transportationsales"                      , "Transportation Sales       (MWh)"),
    ("transportationCustomers"        , "transportationcustomers"                  , "Transportation Customers        "),
    ("transportationPrice"            , "transportationprice"                      , "Transportation Price (cents/kWh)"),
    ("totalRevenue"                   , "totalrevenue"                             , "total Revenue              ($1K)"),
    ("totalSales"                     , "totalsales"                               , "total Sales                (MWh)"),
    ("totalCustomers"                 , "totalcustomers"                           , "total Customers                 "),
    ("totalPrice"                     , "totalprice"                               , "total Price          (cents/kWh)")
]

SQL_ALIASES = [(x[0], x[1]) for x in ALIASES]
DISPLAY_ALIASES = [(x[0], x[2]) for x in ALIASES]

DICTIONARY_KEYS_ORDERED = [x[0] for x in DISPLAY_ALIASES]
DICTIONARY_KEYS_EMMISIONS_INDEXES = range(2,8)
DICTIONARY_KEYS_PRICES_INDEXES = range(8,len(DICTIONARY_KEYS_ORDERED))
