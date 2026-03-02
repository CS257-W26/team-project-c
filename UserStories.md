# User Stories
## Feature 1: State Comparisons

* User story: As a user, I want to see two states' statistics side by side so that they can be compared
* Acceptance Criteria: If the user chooses to compare the states of KS and MN then a compared generation value of 9,319,563,787 kwh will be displayed and a compared Co2 tons value of 2,809,662.
* Acceptance Test is in the test_tableMaker.py file in the class TestTableOutputUserStories in function test_two_state_display

## Feature 2: Data Display for entire USA

* User story: As a user I want to see price data for the entire US so that I am more informed.
* Acceptance Criteria: When the user selects US data to be displayed (through command_line or website), then a generation value of 2,564,933,709,972 kwh and a total price of 13.73 cents/kwh will be displayed. 
* Acceptance Test is in the test_tableMaker.py file in the class TestTableOutputUserStories in function test_us_display

## Feature 3: Individual State Displays

* User story: As a user I want to see data for a specific state so that I am more informed about energy consumption for each state.
* Acceptance Criteria: When the user selects Minnesota as the state who's data is to be displayed then a Co2 emissions value of 22,476,702 tons and a totalRevenue 7,971,414.76 ($1k) will be displayed.
* Acceptance Test is in the test_tableMaker.py file in the class TestTableOutputUserStories in function test_single_state_display
