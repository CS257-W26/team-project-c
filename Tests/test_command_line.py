'''
File contains tests for command_line.py 
'''
import sys
import unittest
from io import StringIO
from command_line import main
from Tests.test_constants import VALID_CA_TABLE, VALID_WA_NM_TABLE


if __name__ == '__main__':
    unittest.main()

class TestCommandLine(unittest.TestCase):
    #self.maxDiff=None
    """Full stack tests for the command_line"""
    def test_one_state(self):
        """test one state input"""
        sys.argv = ['command_line.py', 'CA']
        sys.stdout = StringIO()
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, VALID_CA_TABLE)
    def test_multiple_states(self):
        """test two states and US because why not knock two birds with one stone""" 
        sys.argv = ['command_line.py', 'WA', 'NM']
        sys.stdout = StringIO()
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, VALID_WA_NM_TABLE)
