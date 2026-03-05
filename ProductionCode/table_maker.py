"""this class manages managing and formatting tables for the command line
Each entry has two required fields"""

import io
from ProductionCode.data_processing import format_string
from ProductionCode.config import DISPLAY_ALIASES

class TableMaker:
"""Class to construct text formatted tables for command line interface"""

    def __init__(self, data=None):
        """
        contructor
        param data: data to be displayed in the table (optional)
        """
        if data is None:
            data = []
        self.entries = []
        for entry in data:
            if entry.get('state') == 'comparison':
                self.add_comparison_entry(entry)
            else:
                self.add_new_entry(entry)

    def add_new_empty_entry(self, state, year):
        """
        Adds a new empty entry for the state and year. If one exists throws an error
        param state: two letter state code of entry to create
        param year: year of entry to create
        """
        for entry in self.entries:
            if entry.get("state") == state and entry.get("year") == year:
                raise KeyError("Entry already exists")
        self.entries.append({"state" : state, "year" : year})

    def add_new_entry(self, entry):
        """
        Add a new entry. Throws an error if one already exists for state, year
        entry is a dictionary, must contain "state" and "year".
        Dictionary entries not listed in display Alliases will not be printed
        param entry: dictionary containing data for a new entry. Must include state and year
        """
        if not isinstance(entry, dict):
            raise TypeError("Entry must be of <class 'dict'>")
        for row in self.entries:
            if row.get("state") == entry.get("state") and row.get("year") == entry.get("year"):
                raise KeyError("Entry already exists")
        self.entries.append(entry)

    def add_data_for_entry(self, state, year, data):
        """
        Adds a new data entry for the state and year.
        raises an error if entry for state and year does not exist 
        param state: state to put data under
        param year: year to put data under
        param data: a tuple (key, data) and key must be an acceptable key for this class
        (See DISPLAY_ALIASES)
        """
        if not isinstance(data, tuple):
            raise TypeError("Data must be a tuple of (key, value)")
        for entry in self.entries:
            if entry.get("state") == state and entry.get("year") == year:
                entry[data[0]] = data[1]
                return
        raise KeyError("Entry does not exists")

    def add_comparison_entry(self, entry):
        """
        Add a new comparison. Throws an error if key state != 'comparison'
        Dictionary entries not listed in display Alliases will not be printed
        param entry: a dictionary of comparison data, must contain 'state': 'comparison'.
        """
        if not isinstance(entry, dict):
            raise TypeError("Entry must be of <class 'dict'>")
        if entry.get('state') != 'comparison':
            raise KeyError("'state' must have value 'comparison'")
        self.entries.append(entry)

    def get_table(self):
        """
        Get the formated table
        return table_str: table formated as a string"""   
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
        """
        Returns a fromated row for the table
        param alias: tuple containing key to search for and lable to display on this row
        param col_sizes: array of ints specifying the width of each col
        return line: a row of the table formated as a string.
        """
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
        """
        Returns True if one or more entries is present in a row.
        param row_name: key for row that we want to test
        return: Boolean"""
        for entry in self.entries:
            if entry.get(row_name) is not None:
                return False
        return True

    def get_col_sizes(self):
        """
        Gets the width for each col based on the widest piece of data (character wise)
        returns sizes: array of ints specifying each column's size
        """
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
