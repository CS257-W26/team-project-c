"""this class manages managing and formatting tables for the command line
Each entry has two required fields"""

import io

#variables
displayAlliases = [
    ("state"                          , "State                           "),
    ("year"                           , "Year                            "),
    ("generation"                     , "Generation                 (kWh)"),
    ("thermalOutput"                  , "Useful Thermal Output    (MMBtu)"),
    ("totalFuelConsumption"           , "Total Fuel Consumption   (MMBtu)"),
    ("totalFuelConsumptionGeneration" , "Total Fuel Consumption for      |\nElectric Generation      (MMBtu)"),
    ("co2Tons"                        , "CO2 Emmissions            (Tons)"),
    ("co2MetricTons"                  , "CO2 Emmissions     (Metric Tons)"),
    ("residentialRevenue"             , "Residential Revenue        ($1K)"),
    ("residentialSales"               , "Residential Sales          (MWh)"),
    ("residentialCustomers"           , "Residential Customers           "),
    ("residentialPrice"               , "Residential Price    (cents/kWh)"),
    ("commercialRevenue"              , "Commercial Revenue         ($1K)"),
    ("commercialSales"                , "Commercial Sales           (MWh)"),
    ("commercialCustomers"            , "Commercial Customers            "),
    ("commercialPrice"                , "Commercial Price     (cents/kWh)"),
    ("industrialRevenue"              , "Industrial Revenue         ($1K)"),
    ("industrialSales"                , "Industrial Sales           (MWh)"),
    ("industrialCustomers"            , "Industrial Customers            "),
    ("industrialPrice"                , "Industrial Price     (cents/kWh)"),
    ("transportationRevenue"          , "Transportation Revenue     ($1K)"),
    ("transportationSales"            , "Transportation Sales       (MWh)"),
    ("transportationCustomers"        , "Transportation Customers        "),
    ("transportationPrice"            , "Transportation Price (cents/kWh)"),
    ("totalRevenue"                   , "total Revenue              ($1K)"),
    ("totalSales"                     , "total Sales                (MWh)"),
    ("totalCustomers"                 , "total Customers                 "),
    ("totalPrice"                     , "total Price          (cents/kWh)")
]

class TableMaker:

    """each entry is a dictionary"""
    def __init__(self):
        self.entries = []

    def addNewEmptyEntry(self, state, year):
        """Adds a new empty entry for the state and year. If one exists throws an error"""
        for entry in self.entries:
            if entry.get("state") == state and entry.get("year") == year:
                raise KeyError("Entry already exists")
                return
        self.entries.append({"state" : state, "year" : year})

    def addNewEntry(self, entry):
        """add a new entry. Throws an error if one already exists for state, year
        entry is a dictionary, must contain "state" and "year". dictionary entries not listed in display Alliases will not be printed"""
        if type(entry) is not dict:
            raise TypeError("Entry must be of <class 'dict'>")
        for row in self.entries:
            if row.get("state") == entry.get("state") and row.get("year") == entry.get("year"):
                raise KeyError("Entry already exists")
                return
        self.entries.append(entry)

    def addDataForEntry(self, state, year, data):
        """adds a new data entry for the state and year. raises an error if entry for state and year does not exist
        data is a tuple (key, data) key must be an acceptable key for this class. See displayAlliases"""
        if type(data) is not tuple:
            raise TypeError("Data must be a tuple of (key, value)")
        for entry in self.entries:
            if entry.get("state") == state and entry.get("year") == year:
                entry[data[0]] = data[1]
                return
        raise KeyError("Entry does not exists")



    def printTable(self):
        """Displays the table""" 
        
        buffer = io.StringIO()

        colSizes = self.getColSizes();

        for i in range(0,len(displayAlliases)):
            if self.isFullRowEmpty(displayAlliases[i][0]):
                continue
            line = displayAlliases[i][1]
            for j in range(0, len(self.entries)):
                if self.entries[j].get(displayAlliases[i][0]) == None:
                    line += f"| {'NULL':<{colSizes[j]}}"
                else:
                    try:
                        value = float(self.entries[j].get(displayAlliases[i][0]))
                        #value = f"{float(self.entries[j].get(displayAlliases[i][0])):,.2f}"
                        if value % 1 == 0: 
                            line += f"| {int(value):<{colSizes[j]}}"
                        else:
                            value = f"{value:,.2f}"
                            line += f"| {value:<{colSizes[j]}}"
                    except ValueError:
                        value = self.entries[j].get(displayAlliases[i][0])
                        line += f"| {value:<{colSizes[j]}}"
            buffer.write(line + "\n")

            if i == 1:
                buffer.write("--------------------------------")
                for size in colSizes:
                    buffer.write("|" + "-" * (size+1))
                buffer.write("\n")

        print(buffer.getvalue())
        buffer.close()

    def isFullRowEmpty(self, rowName):
        """returns True if one or more entries is present in a row"""
        for entry in self.entries:
            if entry.get(rowName) != None:
                return False
        return True

    def getColSizes(self):
        sizes = []
        for entry in self.entries:
            largestEntry = 4
            for i in range(0, len(displayAlliases)):
                value = entry.get(displayAlliases[i][0])
                if value == None:
                    continue
                try:
                    value = float(value)
                    if value % 1 == 0:
                        value = str(int(value))
                    else:
                        value = f"{float(value):,.2f}"
                    if len(value) > largestEntry:
                        largestEntry = len(value)
                except ValueError:
                    if len(value) > largestEntry:
                        largestEntry = len(value)
            sizes.append(largestEntry + 1)
        return sizes
