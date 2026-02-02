"""This module contains functions and litterals for data formatting and stripping"""

from production_code.config import DICTIONARY_KEYS_ORDERED
from production_code.config import DICTIONARY_KEYS_EMMISIONS_INDEXES
from production_code.config import DICTIONARY_KEYS_PRICES_INDEXES

DECIMAL_PLACES = 2

def format_string(string):
    """returns a formatted string from a string input
    if value is an int -> truncates and adds ,s
    if value is a float -> truncates to DECIMAL_PLACES and add ,s
    if it cant be interperated as either -> return entry"""
    try:
        value = float(string)
        if value % 1 == 0:
            value = f"{int(value):,.0f}"
        else:
            value = f"{float(value):,.{DECIMAL_PLACES}f}"
        return value
    except ValueError:
        return string

def to_num_or_zero(entry):
    '''
    Docstring for self.to_num_or_zero
    converts the entry for the data into a numeric type
    :param entry: the value to be converted
    :return : returns the value as a float
    '''
    if entry is None:
        return 0
    if isinstance(entry, (int, float)):
        value = float(entry)
    elif isinstance(entry, str):
        entry = entry.strip().strip('"')
        if entry in (".", ""):
            return 0
        entry = entry.replace(",", "")
        try:
            value = float(entry)
        except ValueError:
            return 0
    if value.is_integer():
        return int(value)
    return round(value, 2)

def filter_entry(entry, flags):
    '''
    filters data out of entry based on flags.
    :param entry: dict to be filtered
    :param flags: what data to include/ommit [prices, emmisions]
    :retrun: filtered dict
    '''
    if not flags[0]:
        for i in DICTIONARY_KEYS_PRICES_INDEXES:
            try:
                entry.pop(DICTIONARY_KEYS_ORDERED[i])
            except KeyError:
                pass
    if not flags[1]:
        for i in DICTIONARY_KEYS_EMMISIONS_INDEXES:
            try:
                entry.pop(DICTIONARY_KEYS_ORDERED[i])
            except KeyError:
                pass
    return entry
