"""flask app for website navigation and rendering"""

import io
import base64

from flask import Flask, request, render_template, url_for, redirect
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from ProductionCode import core
from ProductionCode.config import AUTOCOMPLETE_OPTIONS, AUTOCOMPLETE_ALLIASES
from ProductionCode.config import AVAILABLE_YEARS, DISPLAY_ALIASES
from ProductionCode.table_maker import TableMaker

app = Flask(__name__)

def get_table(data):
    """Makes a table object and returns the string."""
    my_table = TableMaker()
    my_table.add_new_entry(data)
    return my_table.get_table()

def make_price_plot_base64(state_data):
    categories = ["Residential", "Commercial", "Industrial", "Transportation", "Total"]
    values = [
        state_data.get("residentialPrice", 0),
        state_data.get("commercialPrice", 0),
        state_data.get("industrialPrice", 0),
        state_data.get("transportationPrice", 0),
        state_data.get("totalPrice", 0),
    ]

    fig = Figure(figsize=(7.5, 4.5))
    axis = fig.add_subplot(1, 1, 1)
    axis.bar(categories, values)
    axis.set_title("Average Electricity Price by Sector")
    axis.set_ylabel("cents / kWh")
    axis.tick_params(axis='x', labelrotation=25)

    fig.tight_layout()

    png_output = io.BytesIO()
    FigureCanvas(fig).print_png(png_output)
    return base64.b64encode(png_output.getvalue()).decode("utf-8")

@app.route('/')
def homepage():
    """Route for hompage"""
    return render_template('index.html', autocomplete=AUTOCOMPLETE_OPTIONS, \
        available_years=AVAILABLE_YEARS)

@app.route('/map')
def map()
    '''route for interactive map'''
    return render_template('map.html', autocomplete=AUTOCOMPLETE_OPTIONS, \
        available_years=AVAILABLE_YEARS)

@app.route('/search', methods=['POST'])
def search():
    """route for primary search functionality"""
    state = request.form['state']
    state_index = AUTOCOMPLETE_OPTIONS.index(state)
    state_code = AUTOCOMPLETE_ALLIASES[state_index]
    return redirect(url_for('bystate', state=state_code, year=request.form['year']))

@app.route('/bystate/<state>/<year>/')
def bystate(state, year):
    """Route for individual state data page."""
    state_data = core.get_state_year_data(state, year)
    table_str = get_table(state_data)
    plot_png = make_price_plot_base64(state_data)

    return render_template(
        'bystate.html',
        autocomplete=AUTOCOMPLETE_OPTIONS,
        autocomplete_aliases=AUTOCOMPLETE_ALLIASES,
        available_years=AVAILABLE_YEARS,
        state=state_data.get("state", state),
        year=year,
        table=table_str,
        plot_png=plot_png
    )

@app.route('/compareutility', methods=['GET', 'POST'])
def compareutility():
    """route for handeling getting and routing comparisons"""
    if request.method == 'GET':
        state1 = request.args.get('state1')
        if (state1 is not None):
            state1 = AUTOCOMPLETE_OPTIONS[AUTOCOMPLETE_ALLIASES.index(state1)]
        return render_template('compareutility.html', autocomplete=AUTOCOMPLETE_OPTIONS, \
            available_years=AVAILABLE_YEARS, state1_autofill=state1)
    #POST
    state1 = request.form['state1']
    state2 = request.form['state2']
    state1_index = AUTOCOMPLETE_OPTIONS.index(state1)
    state2_index = AUTOCOMPLETE_OPTIONS.index(state2)
    agg_state_code = AUTOCOMPLETE_ALLIASES[state1_index] + AUTOCOMPLETE_ALLIASES[state2_index]
    return redirect(url_for('compare_states', states=agg_state_code, year=request.form['year']))

@app.route('/compare/<states>/<year>/')
def compare_states(states, year):
    """route for comparison page"""
    data = core.get_comparison(states, year)
    #TODO_later restructure the following when moving to graphs
    keys = [x[0] for x in DISPLAY_ALIASES]
    labels = [x[1] for x in DISPLAY_ALIASES]
    return render_template('compare.html', keys=keys, labels=labels, \
        state1data=data[0], state2data=data[1], comparison=data[2], \
        autocomplete=AUTOCOMPLETE_OPTIONS, available_years=AVAILABLE_YEARS)

@app.route('/us', methods=['GET', 'POST'])
def display_us_data():
    '''
    Endpoint for displaying US data
    '''
    years = [2013,2014,2015,2016,2017,2018,2019,2020, 2021, 2022, 2023, 2024] 
    selected_year =  request.args.get("year", type=int)
    data = None
    table_str = None
    if selected_year:
        data = core.get_us_year_data(selected_year)
        table_str = get_table(data)
    return render_template('us.html',us_data = data,years = years,selected_year=selected_year, 
                           autocomplete=AUTOCOMPLETE_OPTIONS, available_years=AVAILABLE_YEARS)

@app.errorhandler(404)
def page_not_found(e):
    """handle 404 errors"""
    return render_template('error.html', errorNumber=404, errorText="""
    Uh oh! The page you are looking for does not exist. Try going back to the homepage. 
    <br>""" + str(e),
    autocomplete=AUTOCOMPLETE_OPTIONS, available_years=AVAILABLE_YEARS), 404

@app.errorhandler(500)
def server_error(e):
    """handle 500 errors"""
    return render_template('error.html', errorNumber=500, errorText="""
    Uh oh! There was an internal server error. Sorry for the inconveniance.
    Try visiting our homepage.<br>""" + str(e),
    autocomplete=AUTOCOMPLETE_OPTIONS, available_years=AVAILABLE_YEARS), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5112)
