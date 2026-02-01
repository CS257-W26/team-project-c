'''
File contains tests for command_line.py 
'''
import unittest
from command_line import main
from test_constants import valid_ca_table, valid_ga_e_table, valid_wa_nm_table
import sys
from io import StringIO

if __name__ == '__main__':
    unittest.main()

class TestCommandLine(unittest.TestCase):
    """Full stack tests for the command_line"""
    def test_one_state(self):
        """test one state input"""
        sys.argv = ['command_line.py', 'CA']
        sys.stdout = StringIO()
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, valid_ca_table)
    def test_one_state_flags(self):
        """test one state with flags"""
        sys.argv = ['command_line.py', '-e', 'GA']
        sys.stdout = StringIO()
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, valid_ga_e_table)
    def test_multiple_states(self):
        """test two states and US because why not knock two birds with one stone""" 
        sys.argv = ['command_line.py', 'WA', 'NM']
        sys.stdout = StringIO()
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, valid_wa_nm_table)