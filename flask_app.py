'''
The eventual location for the Flask app interface for the project.
'''
from flask import Flask, Blueprint, render_template_string
from ProductionCode.data_class import Data
from ProductionCode.table_maker import TableMaker
from ProductionCode.config import STATES_LIST

data = Data()
api = Blueprint('api', __name__)
app = Flask(__name__)


def load_data():
    '''
    Loads data into the global data object 
    '''
    data.load_data()

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
    /api/&ltstates&gt/&ltyear&gt/ -> view data for a state
    /api/&ltstates&gt/&ltyear&gt/compare/ -> view data for states with comparisons calulated
    
    &ltstates&gt is a string of two letter state prefixes
    eg. ak mnus kswanm are all valid strings for this field
    Note that emission data is only available for the years 2013-2024
    Price data is available for the years 2010-2025"""
    return f'<pre>{welcome_screen}</pre>'

@api.route('/<string:states>/<string:year>/')
def get_state_year_data(states, year):
    '''Get data for a set of states at year'''
    try:
        state_list = parse_states(states)
    except ValueError:
        return states + " could not be parsed. Make sure it contains only valid states"
    flags = [True] *2
    table = TableMaker()
    table_data = data.get_data(state_list,flags,year)
    for entry in table_data:
        table.add_new_entry(entry)

    return render_template_string(
            """
            <html>
                <body>
                    <pre>{{ table }}</pre>
                </body>
            </html>
            """,
            table=table.get_table()
        )

@api.route('/<string:states>/<string:year>/compare/')
def get_state_year_data_compare(states, year):
    '''Get data for a set of states at year'''
    try:
        state_list = parse_states(states)
    except ValueError:
        return states + " could not be parsed. Make sure it contains only valid states"
    flags = [True] *2
    table = TableMaker()
    table_data = data.get_data(state_list,flags,year)
    for entry in table_data:
        table.add_new_entry(entry)

    return render_template_string(
            """
            <html>
                <body>
                    <pre>{{ table }}</pre>
                </body>
            </html>
            """,
            table=table.get_comparison_table()
        )

@app.errorhandler(404)
def page_not_found(e):
    '''
    Page not found error which displays some helpful info on how to properly input key
    
    :param e: error
    '''
    return ("Sorry, wrong format, do this instead: http://127.0.0.1:5100/api/states/year/ \
            - states: string of consecutive state codes eg. alnmca", 404)

@app.errorhandler(500)
def python_bug(e):
    '''
    If there is a technical bug this will display - hopefully never
    
    :param e: error
    '''
    return ("Uhh oh - technical issue", 500)

if __name__ == "__main__":
    '''
    runs flask app and calls load_data() function
    '''
    app.register_blueprint(api, url_prefix='/api')
    load_data()
    app.run()
