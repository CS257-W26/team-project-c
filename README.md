[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/w6LgLvZq)
# CS257-TeamC
Template for long-term team projects for CS257 Software Design
# Team Members
Rafael 
Gabe
Hongmiao
# Dependencies
Python CSV module - 
Python io module - used for convienience in the TableMaker class
Python argparse module - used for parsing command line input and help management
Python Unittest
# Example
python3 command_line.py -p "MN"
This will display the price data for MN, more states can be added as a space-separated list. "US" is a state and will display the average/aggregate data for the whole US.
python3 command_line.py -h      -> display help information
python3 command_line.py -e CA   -> display emission info for California
python3 command_line.py -c CA MN  -> display emission and price info for California and Minnesota, and their difference in each field
python3 command_line.py US   -> display emission and price info for United States
-- tags can be before or after state list (ie ... US -p  == ... -p US)
# Running Flask app
python3 flask_app.py
The homepage will display information for how to use routes
/api/&ltstates&gt/&ltyear&gt/ -> view data for a state
/api/&ltstates&gt/&ltyear&gt/compare/ -> view data for states with comparisons calulated
    
&ltstates&gt is a string of two letter state prefixes
eg. ak mnus kswanm are all valid strings for this field
Note that emission data is only available for the years 2013-2024
Price data is available for the years 2010-2025