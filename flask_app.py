"""flask app for website navigation and rendering"""

from flask import Flask, request, render_template, url_for, redirect

from ProductionCode import core
from ProductionCode.config import AUTOCOMPLETE_OPTIONS, AUTOCOMPLETE_ALLIASES
from ProductionCode.config import AVAILABLE_YEARS, DISPLAY_ALIASES
from ProductionCode.plotting import PlotBuilder
from flask_api import api

app = Flask(__name__)
plotter = PlotBuilder()

@app.route('/')
def homepage():
    """Route for hompage"""
    return render_template('index.html', autocomplete=AUTOCOMPLETE_OPTIONS, \
        available_years=AVAILABLE_YEARS)

@app.route('/map')
def usmap():
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

@app.route("/bystate/<state>/<year>/")
def bystate(state, year):
    """Route for individual state data page."""
    year_int = int(year)

    state_data = core.get_state_year_data(state, year_int)
    us_data = core.get_us_year_data(year_int)

    return render_template(
        "bystate.html",
        autocomplete=AUTOCOMPLETE_OPTIONS,
        autocomplete_aliases=AUTOCOMPLETE_ALLIASES,
        available_years=AVAILABLE_YEARS,
        state=state_data.get("state", state),
        year=year_int,
        state_data=state_data,
        DISPLAY_ALIASES=DISPLAY_ALIASES,
        price_plot_png=plotter.price_plot_base64(state_data),
        emissions_plot_png=plotter.emissions_plot_base64(state_data, us_data),
    )

@app.route('/compareutility', methods=['GET', 'POST'])
def compareutility():
    """route for handeling getting and routing comparisons"""
    if request.method == 'GET':
        state1 = request.args.get('state1')
        if state1 is not None:
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
    data = core.get_comparison_year(states, year)
    #TODO_later restructure the following when moving to graphs
    keys = [x[0] for x in DISPLAY_ALIASES]
    labels = [x[1] for x in DISPLAY_ALIASES]
    return render_template('compare.html', keys=keys, labels=labels, \
        state1data=data[0], state2data=data[1], comparison=data[2], \
        autocomplete=AUTOCOMPLETE_OPTIONS, available_years=AVAILABLE_YEARS)

@app.route('/us')
def display_us_data():
    '''
    Endpoint for displaying US data
    '''
    selected_year =  request.args.get("year", type=int)
    data = None
    if selected_year:
        data = core.get_us_year_data(selected_year)
    return render_template('us.html',us_data = data,years = AVAILABLE_YEARS,
    selected_year=selected_year, autocomplete=AUTOCOMPLETE_OPTIONS,
    available_years=AVAILABLE_YEARS)

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
    app.register_blueprint(api, url_prefix='/api')
    app.run(host='0.0.0.0', port=5212)
