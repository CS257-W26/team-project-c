"""flask app for website navigation and rendering"""

from flask import Flask, request, render_template, url_for, redirect

from ProductionCode import core
from ProductionCode.config import AUTOCOMPLETE_OPTIONS, AUTOCOMPLETE_ALLIASES
from ProductionCode.config import TITLE_ALIASES, AVAILABLE_YEARS
DATA_OPTIONS = [x[1] for x in TITLE_ALIASES]
from ProductionCode.plotting import PlotBuilder
from flask_api import api

app = Flask(__name__)
plotter = PlotBuilder()

@app.route('/')
def homepage():
    """Route for hompage"""
    return render_template('index.html', autocomplete=AUTOCOMPLETE_OPTIONS)

@app.route('/map')
def usmap():
    '''route for interactive map'''
    return render_template('map.html', autocomplete=AUTOCOMPLETE_OPTIONS)

@app.route('/search', methods=['POST'])
def search():
    """route for primary search functionality"""
    state = request.form['state']
    state_index = AUTOCOMPLETE_OPTIONS.index(state)
    state_code = AUTOCOMPLETE_ALLIASES[state_index]
    return redirect(url_for('bystate', state=state_code))

@app.route("/bystate/<state>/")
def bystate(state):
    """Route for individual state data page."""

    year = request.args.get("year", type=int)
    table_data = None
    if year:
        table_data = core.get_state_year_data(state, year)

    graph_title = request.args.get("graph_title", type=str)
    plot_base64 = None
    if graph_title:
        index = DATA_OPTIONS.index(graph_title)
        graph_title_alias = TITLE_ALIASES[index][0]
        graph_data = core.get_graph_data(state, graph_title_alias)
        plot = PlotBuilder()
        plot.add_data(graph_data)
        plot_base64 = plot.get_fig()

    return render_template(
        "bystate.html",
        autocomplete=AUTOCOMPLETE_OPTIONS,
        data_options=DATA_OPTIONS,
        year_options=AVAILABLE_YEARS,

        state=state,
        selected_graph=graph_title,
        selected_year=year,

        plot_png=plot_base64,
        table_data=table_data,
    )

@app.route('/compareutility', methods=['GET', 'POST'])
def compareutility():
    """route for handeling getting and routing comparisons"""
    if request.method == 'GET':
        state1 = request.args.get('state1')
        if state1 is not None:
            state1 = AUTOCOMPLETE_OPTIONS[AUTOCOMPLETE_ALLIASES.index(state1)]
        return render_template('compareutility.html', autocomplete=AUTOCOMPLETE_OPTIONS, \
            state1_autofill=state1)
    #POST
    state1 = request.form['state1']
    state2 = request.form['state2']
    state1_index = AUTOCOMPLETE_OPTIONS.index(state1)
    state2_index = AUTOCOMPLETE_OPTIONS.index(state2)
    agg_state_code = AUTOCOMPLETE_ALLIASES[state1_index] + AUTOCOMPLETE_ALLIASES[state2_index]
    return redirect(url_for('compare_states', states=agg_state_code))

@app.route('/compare/<states>/')
def compare_states(states):
    """route for comparison page"""

    year = request.args.get("year", type=int)
    table_data = None
    if year:
        table_data = core.get_comparison_year(states, year)

    graph_title = request.args.get("graph_title", type=str)
    plot_base64 = None
    if graph_title:
        index = DATA_OPTIONS.index(graph_title)
        graph_title_alias = TITLE_ALIASES[index][0]
        state_data = core.get_graph_data_comparison(states, graph_title_alias)
        plot = PlotBuilder()
        plot.add_data(state_data[0])
        plot.add_data(state_data[1])
        plot_base64 = plot.get_fig()

    return render_template(
        "compare.html",
        autocomplete=AUTOCOMPLETE_OPTIONS,
        data_options=DATA_OPTIONS,
        year_options=AVAILABLE_YEARS,
        title_aliases=TITLE_ALIASES,

        state1=states[:2],
        state2=states[2:],
        selected_graph=graph_title,
        selected_year=year,

        plot_png=plot_base64,
        table_data=table_data,
    )

@app.route('/us')
def display_us_data():
    '''
    Endpoint for displaying US data
    '''
    graph_title = request.args.get("graph_title", type=str)
    plot_base64 = None
    if graph_title:
        index = DATA_OPTIONS.index(graph_title)
        graph_title_alias = TITLE_ALIASES[index][0]
        data = core.get_graph_data('US', graph_title_alias)
        plot = PlotBuilder()
        plot.add_data(data)
        plot_base64 = plot.get_fig()
    
    year = request.args.get("year", type=int)
    table_data = None
    if year:
        table_data = core.get_us_year_data(year)
    print(table_data)
    
    return render_template('us.html',
        autocomplete=AUTOCOMPLETE_OPTIONS,
        year_options=AVAILABLE_YEARS,
        title_aliases=TITLE_ALIASES,

        selected_year=year,
        selected_graph=graph_title,

        plot_png=plot_base64, 
        table_data=table_data
    )

@app.errorhandler(404)
def page_not_found(e):
    """handle 404 errors"""
    return render_template('error.html', errorNumber=404, errorText="""
    Uh oh! The page you are looking for does not exist. Try going back to the homepage. 
    <br>""" + str(e),
    autocomplete=AUTOCOMPLETE_OPTIONS), 404

@app.errorhandler(500)
def server_error(e):
    """handle 500 errors"""
    return render_template('error.html', errorNumber=500, errorText="""
    Uh oh! There was an internal server error. Sorry for the inconveniance.
    Try visiting our homepage.<br>""" + str(e),
    autocomplete=AUTOCOMPLETE_OPTIONS), 500

if __name__ == '__main__':
    app.register_blueprint(api, url_prefix='/api')
    app.run(host='0.0.0.0', port=5212)
