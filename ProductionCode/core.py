'''Middle module that takes care of DataSource calls and re-packaaging data for front end'''

db = DataSource()

def get_comparison(states, year):
    """returns comparison data at year - currently hard coded"""
    #TODO "states" into states[]
    return db.get_comparison(states, year)

def get_us_year_data(year):
    return db.get_us_year_data(year)

def get_state_year_data(state, year):
    return get_states_data([state], year)
