'''
File contains tests for command_line.py 
'''
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from command_line import main


if __name__ == '__main__':
    unittest.main()

class TestCommandLine(unittest.TestCase):
    """Full stack tests for the command_line"""
    
    @patch('ProductionCode.data_source.DataSource')        
    def test_one_state(self, mock_db_instance):
        """test one state input"""
        sys.argv = ['command_line.py', 'CA']
        sys.stdout = StringIO()
        mock_db_instance.get_states_data.return_value = [{'state': 'CA', 'year': 2024, 'generation': '5000'}]
        main()
        output = sys.stdout.getvalue().strip()
        self.assertIn(output, 'CA')
        self.assertIn(output, '5000')
        self.assertIn(output, 'Generation')
        self.assertIn(output, '------')
                      
    def test_multiple_states(self):
        """test two states and US""" 
        sys.argv = ['command_line.py', 'WA', 'NM']
        sys.stdout = StringIO()
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, VALID_WA_NM_TABLE)
