import argparse
from ProductionCode.table_maker import TableMaker
from ProductionCode.states import states_list

def main():
    parser = argparse.ArgumentParser(
        description='Acesses and displays most recent emmisions and prices data by state.',
        epilog='Example:'
    )
    parser.add_argument('-p', '--prices', action='store_true',
                        help='add prices to output')  
    parser.add_argument('-e', '--emissions', action='store_true',
                        help='add emissions to output') 
    parser.add_argument('args', nargs='*',type=str,
                        help="A space seperated list of states to display,\
use all caps two letter state codes,\
'US' displays the totals/averages for the whole US")
    
    args = parser.parse_args()

    #process flags
    flags = [False] * 2
    if args.prices or args.emissions:
        flags[0] = args.prices
        flags[1] = args.emissions
    else:
        flags = [True] * 2
    
    #args
    for entry in args.args:
        if entry not in states_list:
            parser.error(entry + " is not a given state. \
Please use uppercase two letter state codes or 'US'")

    myTable = TableMaker()
    
    myTable.add_new_entry({"state": "MN", "year": "1990"})
    myTable.add_new_entry({"state": "WY", "year": "2005" , "totalRevenue" : "1.2"})
    myTable.add_new_empty_entry("US", "2026")
    myTable.add_data_for_entry("US", "2026", ("co2Tons", "50000000"))
    myTable.add_data_for_entry("MN", "1990", ("totalFuelConsumptionGeneration", "100"))
    
    myTable.print_table()




#Hongmiao
#def getData("list of states", "list of flags"):
"""returns array of dicts"""

#Hongmiao
#def getEmmissionsData("State"):

#Rafael
#def getPriceData("State"):
#will have to add up all months for a given year

#Rafael
#def getUSData():

#Rafael
def showHelp(): 
    print("Usage:")


if __name__ == "__main__":
    main()
