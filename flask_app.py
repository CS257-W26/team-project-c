'''
The eventual location for the Flask app interface for the project.
'''
from flask import Flask, Blueprint, render_template_string, abort
from ProductionCode.data_class import Data
from ProductionCode.table_maker import TableMaker

data = Data()
api = Blueprint('api', __name__)
app = Flask(__name__)


def load_data():
    '''
    Loads data into the global data object 
    '''
    data.load_data()

@app.route('/')
def homepage():
    '''
    Homepage which displays some useful information
    '''
    return ("Welcome to the homepage, to access data from the dataset use /api/US2025 \n" \
    " - The data retrieved will be two letter state code with the year of data desired. \n" \
    "Note that emission data is only available for the years 2013-2024\n" \
    "Price data is available for the years 2010-2025\n", 200)

def make_table(entry: dict) -> TableMaker:
    '''
    Helper function which makes a TableMaker Object
    
    :param entry: dictionary that contains info for state year 
        - key in data.data_dict[KS2024] for example
    '''
    table = TableMaker()
    table.add_new_entry(entry)
    return table

@api.route('/<string:key>/')
def get_year_data(key : str):
    '''Get data for key in url'''
    try:
        entry = data.data_dict[key]
        table = make_table(entry)
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
    except Exception:
        abort(500)

@app.errorhandler(404)
def page_not_found(e):
    '''
    Page not found error which displays some helpful info on how to properly input key
    
    :param e: error
    '''
    return ("Sorry, wrong format, do this instead: http://127.0.0.1:5100/api/key/ \
            - key: two letter state code and year ie US2025", 404)

@app.errorhandler(500)
def python_bug(e):
    '''
    If there is a technical bug this will display - hopefully never
    
    :param e: error
    '''
    return ("Uhh oh - technical issue", 500)

if __name__ == '__main__':
    '''
    runs flask app and calls load_data() function
    '''
    app.register_blueprint(api, url_prefix='/api')
    load_data()
    app.run(port=5100)
