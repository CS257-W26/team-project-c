[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/w6LgLvZq)
# CS257-TeamC
Template for long-term team projects for CS257 Software Design
# Team Members
Rafael 
Gabe
Hongmiao
# Dependencies
Python io module - used for convienience in the TableMaker class
argparse - used for parsing command line input and help management
Unittest - Testing
Flask - Flask api and web interface
matplotlib - webapp graphs

# command_line
Example:
python3 command_line.py -p "MN"
This will display the price data for MN, more states can be added as a space-separated list. "US" is a state and will display the average/aggregate data for the whole US.
python3 command_line.py -h      -> display help information
python3 command_line.py -y 2013 CA   -> display info for California in 2013
python3 command_line.py -c CA MN  -> display 2024 info for California and Minnesota, and their difference in each field
python3 command_line.py US   -> display emission and price info for United States
-- tags can be before or after state list (ie ... US -c  == ... -c US)
# flask_api
python3 flask_app.py
/ -> The homepage will display information for how to use routes
/api/allus/year/ -> view data for all the us
/api/bystate/state/year/ -> view data for a state
/api/compare/states/year/ -> view data for states with comparisons calulated.
    
states is a string of two letter state prefixes
eg. ak mnus kswa are all valid strings for this field
Note that emission data is only available for the years 2013-2024
Price data is available for the years 2010-2025"""
## Examples
### Feature 1
/api/compare/CATX/2024/ -> gets info for CA and TX and adds shows net differences
### Feature 2
/api/allus/2023 -> gets info for the enire US for 2023
### Feature 3
/api/bystate/KS/2025 -> gets info for KS in 2025 

# flask_app
Run flask app and view through your web browser.
## Features
### Feature 1
Go to compare page using bottom in top nav bar 
### Feature 2 
Using search bar in navbar search for state and select year
### Feature 
Go to all-us page using all us button in nav bar

## Scanning
Our website enables scanning, there are bullet points and there are clear headings on every page.

## Satisficing
We have a search bar which users can go straight to look for whatever data they want, as well as from individual state page they can go to making comparisons which is satisfisable. 

## Muddling through
If a user enters a bad entry into search bar it will tell the user to use the autofill in order to get the state to load. 

# TD 5 Improvements
## Code Refactoring
### DataSource
DataSource was not a singleton which may have resulted in multiple instances of DataSource objects which would have been a waste of memory.
Fix: Made DataSource a singleton in ProductionCode/data_source.py by overiding the "__new__" function and adding an instance variable to the class on lines 15-21. Also added a test in Tests/test_data_source.py on lines 9-13 which checks that DataSource is now a singleton.

### plotting.py
All of the plotting with matplotlib was in functions in the flask_app file which was not ideal. In order to fix this added a new file, ProductionCode/plotting.py, which made a plot class in order to better handle making graphs for the different web pages. Moved all of the code related to plotting from flask_app which was lines 16-90 to ProductionCode/plotting.py and made a plotbuilder object in flask_app to be used. 

## UI improvements
### Buttons and Stuff
Made all buttons across site have same styling as well as increased the size of all the buttons, also improved look of all dropdowns and search bars. On home page added functionality to navigate to other pages on main section of homepage instead of everything being through header. (Since during ui testing everyone was just looking straight to main part of page to try to find info) Also added a button on the US data page to compare with another state to help show that the US can be queried on the compare page.

### Graphs
We added graphs to all the main data pages: bystate, allus, and compare! This allows the user to view changes in data over time not just for a given year.