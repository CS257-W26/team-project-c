'''
The eventual location for the Flask app interface for the project.
'''
from flask import Flask, Blueprint
from ProductionCode.config import STATES_LIST
import ProductionCode.core as core

api = Blueprint('api', __name__)
app = Flask(__name__)

@api.route('/')
def homepage():
    '''
    Endpoint for our homepage - returns text for welcome screen
    '''
    welcome_screen = """Welcome to the homepage.
    Use the following routes:
    / -> this page
    /api/allus/2023/ -> view data for all the us
    /api/bystate/MN/2024/ -> view data for a state
    /api/compare/MNKS/2023/ -> view data for states with comparisons calulated
    
    &ltstates&gt is a string of two letter state prefixes
    eg. ak mnus kswa are all valid strings for this field
    Note that emission data is only available for the years 2013-2024
    Price data is available for the years 2010-2025"""
    return f'<pre>{welcome_screen}</pre>'

@api.route('/allus/<int:year>/')
def get_all_us_data(year):
    '''gets data for the whole US at a given year
    :param year: int of the year to get data for
    :return dictionary with us data
    '''
    result = core.get_us_year_data(year)
    return result

@api.route('/bystate/<string:state>/<int:year>/')
def get_state_data(state, year):
    '''gets data for a single state at a given year
    :param state: string of the two letter state code to get data for
    :param year: int of the year to get data for
    :return dictionary containing state data for specific year
    '''
    state = state.upper()
    if len(state) != 2 or state not in STATES_LIST:
        return state + " could not be parsed. Make sure it contains only valid states"
    state_dict_list = core.get_states_data(state, year)
    return state_dict_list[0]

@api.route('/compare/<string:states>/<int:year>/')
def get_comparison_data(states, year):
    '''gets comparison data for a set of states at a given year
    :param states: string of two letter state codes to get data for
    :param year: int of the year to get data for
    :return states_dict list of dictionaries
    '''
    try:
        states_dicts = core.get_comparison(states, year)
    except ValueError:
        return states + " could not be parsed. Make sure it contains only valid states"
    return states_dicts


@app.errorhandler(404)
def page_not_found(e):
    '''
    Page not found error which displays some helpful info on how to properly input key
    
    :param e: error
    :return error statement
    '''
    return (f"Sorry, wrong format, do this instead: http://127.0.0.1:5100/api/states/year/ \
            - states: string of consecutive state codes eg. alnm \
            - error: {e}", 404)

@app.errorhandler(500)
def python_bug(e):
    '''
    If there is a technical bug this will display - hopefully never
    
    :param e: error
    :return error statement
    '''
    return (f"Uhh oh - technical issue: {e}", 500)

def main():
    '''runs flask app'''
    app.run(host='0.0.0.0', port=5112)

if __name__ == "__main__":
    main()
