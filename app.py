"""flask app for website navigation and rendering"""

from flask import Flask, request, render_template, url_for, redirect
from ProductionCode import core
from ProductionCode.config import AUTOCOMPLETE_OPTIONS, AUTOCOMPLETE_ALLIASES
from ProductionCode.config import AVAILABLE_YEARS, DISPLAY_ALIASES

app = Flask(__name__)

@app.route('/')
def homepage():
    """Route for hompage"""
    return render_template('index.html', autocomplete=AUTOCOMPLETE_OPTIONS, \
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
    """route for individual state data page"""
    return render_template('bystate.html', autocomplete=AUTOCOMPLETE_OPTIONS, \
        available_years=AVAILABLE_YEARS, state=state, year=year)

@app.route('/compareutility', methods=['GET', 'POST'])
def compareutility():
    """route for handeling getting and routing comparisons"""
    if request.method == 'GET':
        #TODO_later add some sort of autopopulate to compare utility state1
        #field if we get /compareutility?state1=<XX> via bystate page
        return render_template('compareutility.html', autocomplete=AUTOCOMPLETE_OPTIONS, \
            available_years=AVAILABLE_YEARS)
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

@app.errorhandler(404)
def page_not_found(e):
    """handle 404 errors"""
    return render_template('error.html', errorNumber=404, errorText="""
    Uh oh! The page you are looking for does not exist. Try going back to the homepage. 
    <br>""" + str(e)), 404

@app.errorhandler(500)
def server_error(e):
    """handle 500 errors"""
    return render_template('error.html', errorNumber=500, errorText="""
    Uh oh! There was an internal server error. Sorry for the inconveniance.
    Try visiting our homepage.<br>""" + str(e)), 500

if __name__ == '__main__':
    app.run()
