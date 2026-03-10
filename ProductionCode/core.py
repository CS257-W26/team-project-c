'''
Middle module that takes care of DataSource calls
re-packaaging/formating data for front end, and interperating
the <states> part of url routes'''

from ProductionCode.data_source import DataSource
from ProductionCode.config import STATES_LIST
from ProductionCode.data_processing import format_string


def _get_db():
    '''Creates DataSource'''
    return DataSource()

def parse_states(states: str):
    """
    All the api and website urls use the format of two state codes
    concatinated. eg CAAK for California and Alaska. However, the 
    backend uses arrays of these codes. This function converts them
    Param: states (str) string containing two letter state codes
    Returns: parsed [(str)] array of two letter state codes in all caps
    throws: ValueError when the string has an incorrect state code
    """
    parsed = []
    if len(states)%2 == 1 and len(states) in range(1,4):
        raise ValueError(states + " could not be parsed")
    for i in range(0, len(states), 2):
        state_code = (states[i] + states[i+1]).upper()
        if state_code not in STATES_LIST:
            raise ValueError(state_code + " is not a state code")
        parsed.append(state_code)
    return parsed

def get_comparison_year(states, year):
    '''
    gets comparison data at year
    param states str: string of two letter state codes to get data for
    param year int: year to get data for
    return states list of dicts of data for a year
    '''
    states = parse_states(states)
    db = _get_db()
    states = db.get_comparison(states, year)
    for state in states:
        for key in state:
            if key != 'year':
                state[key] = format_string(state[key])
    return states

def get_us_year_data(year):
    '''
    Gets us year data
    param year int: year to get data for
    return data: dict of data for a year
    '''
    db = _get_db()
    data = db.get_us_year_data(year)
    for key in data:
        if key != 'year':
            data[key] = format_string(data[key])
    return data

def get_state_year_data(state, year):
    '''
    Get state data for year
    param state str: two letter state code of state to get data for
    param year int: year to get data for
    return data: dict of data for a year
    '''
    db = _get_db()
    data = db.get_states_data([state], year)[0]
    for key in data:
        if key != 'year':
            data[key] = format_string(data[key])
    return data

def get_states_year(states, year):
    '''
    Get data for a year for passed states
    param states list: list of two letter state code of states to get data for
    param year int: year to get data fro 
    return data: list of dicts of data for states
    '''
    db=_get_db()
    results = db.get_states_data(states, year)
    return results

def get_graph_data(state, graph_type):
    '''
    Gets the data for a graph
    param state str, state code of state to get data for
    param graph_type str, desired data to get. Must be a value in config.py DICTIONARY_KEYS_ORDERED
    return: list containing info for graph
    '''
    db=_get_db()
    data = db.get_graphable_data(state, graph_type)
    for i, _ in enumerate(data[2:], start=2):
        data[i] = float(data[i])
    return data
