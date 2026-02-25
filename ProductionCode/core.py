'''
Middle module that takes care of DataSource calls
re-packaaging/formating data for front end, and interperating
the <states> part of url routes'''

from ProductionCode.data_source import DataSource
from ProductionCode.config import STATES_LIST
from ProductionCode.data_processing import format_string


db = DataSource()

def parse_states(states):
    """
    All the api and website urls use the format of two state codes
    concatinated. eg CAAK for California and Alaska. However, the 
    backend uses arrays of these codes. This function converts them
    Param: states (str) string containing two letter state codes
    Returns: parsed [(str)] array of two letter state codes in all caps
    throws: ValueError when the string has an incorrect state code
    """
    parsed = []
    if len(states)%2 == 1:
        raise ValueError(states + " could not be parsed")
    for i in range(0, len(states), 2):
        state_code = (states[i] + states[i+1]).upper()
        if state_code not in STATES_LIST:
            raise ValueError(state_code + " is not a state code")
        parsed.append(state_code)
    return parsed

def get_comparison(states, year):
    """returns comparison data at year - currently hard coded"""
    states = parse_states(states)
    states = db.get_comparison(states, year)
    for state in states:
        for key in state:
            state[key] = format_string(state[key])
    return states

def get_us_year_data(year):
    data = db.get_us_year_data(year)
    for key in data:
        data[key] = format_string(data[key])
    return data

def get_state_year_data(state, year):
    data = db.get_states_data([state], year)[0]
    for key in data:
        data[key] = format_string(data[key])
    return data
