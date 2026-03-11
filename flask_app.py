"""flask app for website navigation and rendering"""

from flask import Flask, request, render_template, url_for, redirect

from ProductionCode import core
from ProductionCode.config import AUTOCOMPLETE_OPTIONS, AUTOCOMPLETE_ALLIASES
from ProductionCode.config import  TITLE_ALIASES
DATA_OPTIONS = [x for x in TITLE_ALIASES]
from ProductionCode.plotting import PlotBuilder
from flask_api import api

app = Flask(__name__)
plotter = PlotBuilder()

@app.route('/')
def homepage():
    """Route for hompage"""
    return render_template('index.html', autocomplete=AUTOCOMPLETE_OPTIONS, \
        data_options=DATA_OPTIONS)

@app.route('/map')
def usmap():
    '''route for interactive map'''
    return render_template('map.html', autocomplete=AUTOCOMPLETE_OPTIONS, \
        data_options=DATA_OPTIONS)

@app.route('/search', methods=['POST'])
def search():
    """route for primary search functionality"""
    state = request.form['state']
    state_index = AUTOCOMPLETE_OPTIONS.index(state)
    state_code = AUTOCOMPLETE_ALLIASES[state_index]
    return redirect(url_for('bystate', state=state_code, data_type=request.form['data_type']))

@app.route("/bystate/<state>/<graph_type>/")
def bystate(state, graph_type):
    """Route for individual state data page."""

    state_data = core.get_graph_data(state, graph_type)
    plot = PlotBuilder()
    plot.add_data(state_data)
    plot_base64 = plot.get_fig()

    return render_template(
        "bystate.html",
        autocomplete=AUTOCOMPLETE_OPTIONS,
        autocomplete_aliases=AUTOCOMPLETE_ALLIASES,
        data_options=DATA_OPTIONS,
        state=state_data[0],
        plot_png=plot_base64,
    )

@app.route('/compareutility', methods=['GET', 'POST'])
def compareutility():
    """route for handeling getting and routing comparisons"""
    if request.method == 'GET':
        state1 = request.args.get('state1')
        if state1 is not None:
            state1 = AUTOCOMPLETE_OPTIONS[AUTOCOMPLETE_ALLIASES.index(state1)]
        return render_template('compareutility.html', autocomplete=AUTOCOMPLETE_OPTIONS, \
            data_options=DATA_OPTIONS, state1_autofill=state1)
    #POST
    state1 = request.form['state1']
    state2 = request.form['state2']
    state1_index = AUTOCOMPLETE_OPTIONS.index(state1)
    state2_index = AUTOCOMPLETE_OPTIONS.index(state2)
    agg_state_code = AUTOCOMPLETE_ALLIASES[state1_index] + AUTOCOMPLETE_ALLIASES[state2_index]
    return redirect(url_for('compare_states', states=agg_state_code, data_type=request.form['data_type']))

@app.route('/compare/<states>/<graph_type>/')
def compare_states(states, graph_type):
    """route for comparison page"""

    state_data = core.get_graph_data_comparison(states, graph_type)
    plot = PlotBuilder()
    plot.add_data(state_data[0])
    plot.add_data(state_data[1])
    plot_base64 = plot.get_fig()

    return render_template(
        "compare.html",
        autocomplete=AUTOCOMPLETE_OPTIONS,
        autocomplete_aliases=AUTOCOMPLETE_ALLIASES,
        data_options=DATA_OPTIONS,
        state1=state_data[0][0],
        state2=state_data[1][0],
        plot_png=plot_base64,
    )

@app.route('/us')
def display_us_data():
    '''
    Endpoint for displaying US data
    '''
    graph_type =  request.args.get("graph_type", type=int)
    data = None
    if graph_type:
        data = core.get_graphable_data('US', graph_type)
    plot = PlotBuilder()
    plot.add_data(state_data)
    plot_base64 = plot.get_fig()
    return render_template('us.html',plot_png = plot_base64, data_options=DATA_OPTIONS,
    selected_data=graph_type, autocomplete=AUTOCOMPLETE_OPTIONS,)

@app.errorhandler(404)
def page_not_found(e):
    """handle 404 errors"""
    return render_template('error.html', errorNumber=404, errorText="""
    Uh oh! The page you are looking for does not exist. Try going back to the homepage. 
    <br>""" + str(e),
    autocomplete=AUTOCOMPLETE_OPTIONS, data_options=DATA_OPTIONS), 404

@app.errorhandler(500)
def server_error(e):
    """handle 500 errors"""
    return render_template('error.html', errorNumber=500, errorText="""
    Uh oh! There was an internal server error. Sorry for the inconveniance.
    Try visiting our homepage.<br>""" + str(e),
    autocomplete=AUTOCOMPLETE_OPTIONS, data_options=DATA_OPTIONS), 500

if __name__ == '__main__':
    app.register_blueprint(api, url_prefix='/api')
    app.run(host='0.0.0.0', port=5212)
