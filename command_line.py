'''Command Line functionality'''
import argparse
import sys
from ProductionCode.table_maker import TableMaker
from ProductionCode.config import STATES_LIST
from ProductionCode.data_source import DataSource

def main():
    '''Handles user input with argparse calls data retrival functions, displays to command line'''

    args = parse_input()

    database = DataSource()

    if args.compareMode:
        states_results = database.get_comparison(args.args, args.year)
    elif "US" in args.args:
        states_results = [database.get_us_year_data(args.year)]
    else:
        states_results = database.get_states_data(args.args, args.year)

    my_table = TableMaker(states_results)
    print(my_table.get_table())

def settup_argument_parser():
    """Setsup ArgumentParser object
    :return parser: built argument parser for use in main
    """
    parser = argparse.ArgumentParser(
        description="Acesses and displays most recent emmisions and prices data by state.\n\n\
        Note: no year selection available ... yet",
        epilog='Example: python3 command_line.py -p KS -> will ' \
        'display price information for Kansas in 2024'
    )
    parser.add_argument('-y', '--year', type=int, default=2024,
                        help='select data for given year. Default is 2024')
    parser.add_argument('-c', '--compareMode', action='store_true',
                        help='output displayed with a net +/- as ' \
                        'compared to the first state inputed')
    parser.add_argument('args', nargs='*',type=str,
                        help="A space seperated list of states to display, \
                        use all caps two letter state codes, \
                        'US' displays the totals/averages for the whole US")
    return parser

def parse_input():
    """handles special cases and returns args
    :return args: object that contains user input
    """
    parser = settup_argument_parser()
    args = parser.parse_args()

    #check if no args
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)

    #args
    for entry in args.args:
        if entry not in STATES_LIST:
            parser.error(entry + " is not a given state. \
Please use uppercase two letter state codes or 'US'")
            sys.exit(1)
    return args

if __name__ == "__main__":
    main()
