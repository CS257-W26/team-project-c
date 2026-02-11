'''Command Line functionality'''
import argparse
import sys
from ProductionCode.table_maker import TableMaker
from ProductionCode.config import STATES_LIST
from ProductionCode.data_source import DataSource

def main():
    '''Handles user input with argparse calls data retrival functions, displays to command line'''

    args = parse_input()
    flags = get_flags(args)

    database = DataSource()

    #complete_data = database.get_data(args.args, flags, 2024)
    my_table = TableMaker()
    if ("US" in args.args):
        states_results = database.get_us_year_data(2024)
    else:
        states_results = database.get_states_data(args.args, 2024)

    print(states_results)

    if args.compareMode:
        print(my_table.get_comparison_table())
    else:
        print(my_table.get_table())

def settup_argument_parser():
    """Setsup ArgumentParser object"""
    parser = argparse.ArgumentParser(
        description="Acesses and displays most recent emmisions and prices data by state.\n\n\
        Note: no year selection available ... yet",
        epilog='Example: python3 command_line.py -p KS -> will ' \
        'display price information for Kansas in 2024'
    )
    parser.add_argument('-p', '--prices', action='store_true',
                        help='add prices to output (default is all data)')
    parser.add_argument('-e', '--emissions', action='store_true',
                        help='add emissions to output (default is all data)')
    parser.add_argument('-c', '--compareMode', action='store_true',
                        help='output displayed with a net +/- as ' \
                        'compared to the first state inputed')
    parser.add_argument('args', nargs='*',type=str,
                        help="A space seperated list of states to display, \
                        use all caps two letter state codes, \
                        'US' displays the totals/averages for the whole US")
    return parser

def parse_input():
    """handles special cases and returns args"""
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

def get_flags(args):
    """Creates a list of bools, used by the production code, to retrive filtered data"""
    #process flags : see settup_argument_parser or help screen to see the behavior filter flags
    flags = [False] * 2
    if args.prices or args.emissions:
        flags[0] = args.prices
        flags[1] = args.emissions
    else:
        flags = [True] * 2
    return flags

if __name__ == "__main__":
    main()
