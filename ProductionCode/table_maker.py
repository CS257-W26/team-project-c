"""this class manages managing and formatting tables for the command line
Each entry has two required fields"""

import io
from ProductionCode.data_processing import format_string

#variables
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

class TableMaker:

    """each entry is a dictionary"""
    def __init__(self):
        self.entries = []

    def __init__(self, data):
        self.entries = []
        for entry in data:
            if entry.get('state') == 'comparison':
                add_comparison_entry(entry)
            else:
                add_new_entry(entry)

    def add_new_empty_entry(self, state, year):
        """Adds a new empty entry for the state and year. If one exists throws an error"""
        for entry in self.entries:
            if entry.get("state") == state and entry.get("year") == year:
                raise KeyError("Entry already exists")
        self.entries.append({"state" : state, "year" : year})

    def add_new_entry(self, entry):
        """add a new entry. Throws an error if one already exists for state, year
        entry is a dictionary, must contain "state" and "year".
        Dictionary entries not listed in display Alliases will not be printed"""
        if not isinstance(entry, dict):
            raise TypeError("Entry must be of <class 'dict'>")
        for row in self.entries:
            if row.get("state") == entry.get("state") and row.get("year") == entry.get("year"):
                raise KeyError("Entry already exists")
        self.entries.append(entry)

    def add_data_for_entry(self, state, year, data):
        """adds a new data entry for the state and year.
        raises an error if entry for state and year does not exist 
        data is a tuple (key, data) and key must be an acceptable key for this class
        (See DISPLAY_ALIASES)"""
        if not isinstance(data, tuple):
            raise TypeError("Data must be a tuple of (key, value)")
        for entry in self.entries:
            if entry.get("state") == state and entry.get("year") == year:
                entry[data[0]] = data[1]
                return
        raise KeyError("Entry does not exists")

    def add_comparison_entry(self, entry):
        """add a new comparison. Throws an error if jey state != 'comparison'
        entry is a dictionary, must contain 'state': 'comparison'.
        Dictionary entries not listed in display Alliases will not be printed"""
        if not isinstance(entry, dict):
            raise TypeError("Entry must be of <class 'dict'>")
        if entry.get('state') != 'comparison':
            raise KeyError("'state' must have value 'comparison'")
        self.entries.append(entry)

    def get_table(self):
        """Displays the table"""   
        buffer = io.StringIO()
        col_sizes = self.get_col_sizes()

        for i, alias in enumerate(DISPLAY_ALIASES):
            if self.is_row_empty(alias[0]):
                continue

            buffer.write(self.get_table_row(alias, col_sizes) + "\n")

            if i == 1:
                buffer.write("--------------------------------")
                for size in col_sizes:
                    buffer.write("|" + "-" * (size+1))
                buffer.write("\n")

        table_str = buffer.getvalue()
        buffer.close()
        return table_str

    def get_table_row(self, alias, col_sizes):
        """returns a fromated row for the table"""
        line = alias[1]
        for j, _ in enumerate(self.entries):
            if self.entries[j].get(alias[0]) is None:
                line += f"| {'NULL':<{col_sizes[j]}}"
            else:
                value = self.entries[j].get(alias[0])
                if alias[0] != 'year':
                    value = format_string(value)
                line += f"| {value:<{col_sizes[j]}}"
        return line

    def is_row_empty(self, row_name):
        """returns True if one or more entries is present in a row. Used for print_table()"""
        for entry in self.entries:
            if entry.get(row_name) is not None:
                return False
        return True

    def get_col_sizes(self):
        """gets the width for each col based on the widest piece of data (character wise)"""
        sizes = []
        for entry in self.entries:
            largest_entry = 4
            for alias in DISPLAY_ALIASES:
                value = entry.get(alias[0])
                if value is None:
                    continue
                if alias[0] != 'year':
                    value = format_string(value)
                    largest_entry = max(largest_entry, len(value))
            sizes.append(largest_entry + 1)
        return sizes
