'''
The eventual location for the Flask app interface for the project.
'''
from flask import Flask, Blueprint#, render_template_string
from ProductionCode.data_source import DataSource
#from ProductionCode.table_maker import TableMaker
from ProductionCode.config import STATES_LIST

data = DataSource()
api = Blueprint('api', __name__)
app = Flask(__name__)

def parse_states(states):
    """
    Parses and checks for errors in <states> route string.
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

@app.route('/')
def homepage():
    '''
    Endpoint for our homepage - returns text for welcome screen
    '''
    welcome_screen = """Welcome to the homepage.
    Use the following routes:
    / -> this page
    /api/allus/&ltyear&gt/ -> view data for all the us
    /api/bystate/&ltstate&gt/&ltyear&gt/ -> view data for a state
    /api/compare/&ltstates&gt/&ltyear&gt/ -> view data for states with comparisons calulated
    
    &ltstates&gt is a string of two letter state prefixes
    eg. ak mnus kswa are all valid strings for this field
    Note that emission data is only available for the years 2013-2024
    Price data is available for the years 2010-2025"""
    return f'<pre>{welcome_screen}</pre>'

@api.route('/allus/<int:year>/')
def get_all_us_data(year):
    '''gets data for the whole US at a given year
    param year: int of the year to get data for'''
    result = data.get_us_year_data(year)
    return result

@api.route('/bystate/<string:state>/<int:year>/')
def get_state_data(state, year):
    '''gets data for a single state at a given year
    param state: string of the two letter state code to get data for
    param year: int of the year to get data for'''
    state = state.upper()
    if len(state) != 2 or state not in STATES_LIST:
        return state + " could not be parsed. Make sure it contains only valid states"
    state_dict = data.get_states_data([state], year)
    return state_dict

@api.route('/compare/<string:states>/<int:year>/')
def get_comparison_data(states, year):
    '''gets comparison data for a set of states at a given year
    param states: string of two letter state codes to get data for
    param year: int of the year to get data for'''
    try:
        state_list = parse_states(states)
    except ValueError:
        return states + " could not be parsed. Make sure it contains only valid states"
    states_dict = data.get_comparison(state_list, year)
    return states_dict


@app.errorhandler(404)
def page_not_found(e):
    '''
    Page not found error which displays some helpful info on how to properly input key
    
    :param e: error
    '''
    return (f"Sorry, wrong format, do this instead: http://127.0.0.1:5100/api/states/year/ \
            - states: string of consecutive state codes eg. alnmca \
            - error: {e}", 404)

@app.errorhandler(500)
def python_bug(e):
    '''
    If there is a technical bug this will display - hopefully never
    
    :param e: error
    '''
    return (f"Uhh oh - technical issue: {e}", 500)

def main():
    '''runs flask app and calls load_data() function'''
    app.register_blueprint(api, url_prefix='/api')
    #load_data()
    app.run(host='0.0.0.0', port=5108)

if __name__ == "__main__":
    main()
