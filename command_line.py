import sys
from ProductionCode.tableMaker import TableMaker

"""*US is considered a State*""" 

#variables


#Gabe
def main():
    myTable = TableMaker()
    myTable.addNewEntry({"state": "MN", "year": "1990"})
    myTable.addNewEntry({"state": "WY", "year": "2005" , "totalRevenue" : "1"})
    myTable.addNewEmptyEntry("US", "2026")
    myTable.addDataForEntry("US", "2026", ("co2Tons", "5000"))
    myTable.printTable()


"""Get user input, check user input, Call correct functions, call displaying data"""
"""map flags to list of flags for get data function (--prices, --emmissions)"""

"""list of states and list of tags must only have valid entries"""
"""flags will be a list that describes what filters we want to use, each is a bool"""
"""[prices, emmissions]"""

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
