"""This module contains functions and litterals for data formatting and stripping"""
#from json import dum #Is this needed?
from ProductionCode.config import DICTIONARY_KEYS_ORDERED
from ProductionCode.config import DICTIONARY_KEYS_EMMISIONS_INDEXES
from ProductionCode.config import DICTIONARY_KEYS_PRICES_INDEXES

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
