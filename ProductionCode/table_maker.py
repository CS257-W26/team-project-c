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

    def add_new_empty_entry(self, state, year):
        """Adds a new empty entry for the state and year. If one exists throws an error"""
        for entry in self.entries:
            if entry.get("state") == state and entry.get("year") == year:
                raise KeyError("Entry already exists")
                return
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
                return
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

    def get_table_string(self):
        """Returns the formatted table as a string"""
        buffer = io.StringIO()
        colSizes = self.get_col_sizes()

        for i, alias in enumerate(DISPLAY_ALIASES):
            if self.is_row_empty(alias[0]):
                continue
            line = alias[1]
            for j, _ in enumerate(self.entries):
                if self.entries[j].get(alias[0]) is None:
                    line += f"| {'NULL':<{colSizes[j]}}"
                else:
                    value = self.entries[j].get(alias[0])
                    if alias[0] != 'year':
                        value = self.format_entry(value)
                    line += f"| {value:<{colSizes[j]}}"
            buffer.write(line + "\n")

            if i == 1:
                buffer.write("--------------------------------")
                for size in colSizes:
                    buffer.write("|" + "-" * (size + 1))
                buffer.write("\n")

        table = buffer.getvalue()
        buffer.close()
        return table
    def get_table(self):
        """Displays the table"""   
        buffer = io.StringIO()
        colSizes = self.get_col_sizes()

        for i, alias in enumerate(DISPLAY_ALIASES):
            if self.is_row_empty(alias[0]):
                continue
            
            buffer.write(self.get_table_row(alias, colSizes) + "\n")

            if i == 1:
                buffer.write("--------------------------------")
                for size in colSizes:
                    buffer.write("|" + "-" * (size+1))
                buffer.write("\n")

        table_str = buffer.getvalue()
        buffer.close()
        return table_str

    def get_table_row(self, alias, colSizes):
        """returns a fromated row for the table"""
        line = alias[1]
        for j, _ in enumerate(self.entries):
            if self.entries[j].get(alias[0]) is None:
                line += f"| {'NULL':<{colSizes[j]}}"
            else:
                value = self.entries[j].get(alias[0])
                if alias[0] != 'year':
                    value = format_string(value)
                line += f"| {value:<{colSizes[j]}}"
        return line

    def get_comparison_table(self):
        """adds comparison cols to a table if multiple entries present
        each col is compared with the leftmost col and the difference is displayed eg.
        State                           | WA             | NM             |
        Year                            | 2025           | 2025           |
        --------------------------------|----------------|----------------|----------------
        Generation                 (kWh)| 21,119,893,670 | 20,106,485,132 | -1,013,408,538
        Useful Thermal Output    (MMBtu)| 10,095,169     | 526,233        | -9,568,936
        ...
        """

        buffer = io.StringIO()
        colSizes = self.get_col_sizes()

        comparisons = self.generate_comparisons()
        comparisons_col_sizes = self.get_comparison_col_sizes(comparisons)
        
        for i, alias in enumerate(DISPLAY_ALIASES):
            if self.is_row_empty(alias[0]):
                continue

            line = alias[1]
            for j, _ in enumerate(self.entries):
                #normal data
                if self.entries[j].get(alias[0]) is None:
                    line += f"| {'NULL':<{colSizes[j]}}"
                else:
                    value = self.entries[j].get(alias[0])
                    if alias[0] != 'year':
                        value = format_string(value)
                    line += f"| {value:<{colSizes[j]}}"
                #comparison col
                if j != 0:
                    if alias[0] == 'state' or alias[0] == 'year':
                        line += "|" + ' ' * (comparisons_col_sizes[j-1]+1)
                    elif comparisons[j-1].get(alias[0]) is None:
                        line += f"| {'NULL':<{comparisons_col_sizes[j-1]}}"
                    else:
                        value = comparisons[j-1].get(alias[0])
                        if value > 0:
                            value = "+" + format_string(value)
                        else:
                            value = format_string(value)
                        line += f"| {value:<{comparisons_col_sizes[j-1]}}"

            buffer.write(line + "\n")

            if i == 1:
                buffer.write("--------------------------------")
                for i, size in enumerate(colSizes):
                    buffer.write("|" + "-" * (size+1))
                    if i != 0:
                        buffer.write("|" + "-" * (comparisons_col_sizes[i-1]+1))

                buffer.write("\n")

        table_str = buffer.getvalue()
        buffer.close()
        return table_str

    def generate_comparisons(self):
        """generate a list of dictionaries of comparisons"""
        comparisons = []
        first_entry = self.entries[0]
        for entry in self.entries[1:]:
            comparison = {}
            for alias in DISPLAY_ALIASES[2:]:
                key = alias[0]
                base_val = first_entry.get(key)
                current_val = entry.get(key)
                if base_val is None or current_val is None:
                    continue
                comparison[key] = current_val - base_val
            comparisons.append(comparison)

        return comparisons


    def get_table_row(self, alias, colSizes):
        """returns a fromated row for the table"""
        line = alias[1]
        for j, _ in enumerate(self.entries):
            if self.entries[j].get(alias[0]) is None:
                line += f"| {'NULL':<{colSizes[j]}}"
            else:
                value = self.entries[j].get(alias[0])
                if alias[0] != 'year':
                    value = format_string(value)
                line += f"| {value:<{colSizes[j]}}"
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

    def get_comparison_col_sizes(self, comparisons):
        """gets the width for each col based on the widest piece of data (character wise)"""
        sizes = []
        for entry in comparisons:
            largest_entry = 4
            for alias in DISPLAY_ALIASES[2:]:
                value = entry.get(alias[0])
                if value is None:
                    continue
                elif float(value) > 0:
                    value = format_string(value)
                    largest_entry = max(largest_entry, len(value)+1)
                else:
                    value = format_string(value)
                    largest_entry = max(largest_entry, len(value))
            sizes.append(largest_entry + 1)
        return sizes
    
