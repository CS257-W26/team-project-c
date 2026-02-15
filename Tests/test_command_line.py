'''
File contains tests for command_line.py 
'''
import sys
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from command_line import main


if __name__ == '__main__':
    unittest.main()

class TestCommandLine(unittest.TestCase):
    """Full stack tests for the command_line"""
    
    @patch('command_line.DataSource')        
    def test_one_state(self, mock_db_class):
        """test one state input"""
        sys.argv = ['command_line.py', 'CA']
        sys.stdout = StringIO()
        mock_db_instance = MagicMock()
        mock_db_class.return_value = mock_db_instance
        mock_db_instance.get_states_data.return_value = \
        [{'state': 'CA', 'year': 2024, 'generation': '5000'}]
        main()
        output = sys.stdout.getvalue().strip()
        self.assertIn('CA', output)
        self.assertIn('5,000', output)
        self.assertIn('Generation', output)
        self.assertIn('------', output)

    @patch('command_line.DataSource')
    def test_multiple_states(self, mock_db_class):
        """test two states""" 
        sys.argv = ['command_line.py', 'WA', 'NM']
        sys.stdout = StringIO()
        mock_db_instance = MagicMock()
        mock_db_class.return_value = mock_db_instance
        mock_db_instance.get_states_data.return_value = \
        [{'state': 'WA', 'year': 2023, 'generation': 5000, 'totalSales': 32475},
        {'state': 'NM', 'year': 2023, 'generation': 30000, 'totalSales': 9999999}]
        main()
        output = sys.stdout.getvalue().strip()
        self.assertIn('NM', output)
        self.assertIn('5,000', output)
        self.assertIn('Generation', output)
        self.assertIn('2023', output)
        self.assertIn('32,475', output)
        self.assertIn('------', output)

    @patch('command_line.DataSource')
    def test_compare_states(self, mock_db_class):
        """test two states with compare""" 
        sys.argv = ['command_line.py', '-c', 'WA', 'NM']
        sys.stdout = StringIO()
        mock_db_instance = MagicMock()
        mock_db_class.return_value = mock_db_instance
        mock_db_instance.get_comparison.return_value = \
        [{'state': 'WA', 'year': 2023, 'generation': 5000, 'totalSales': 32475},
        {'state': 'NM', 'year': 2023, 'generation': 30000, 'totalSales': 9999999},
        {'state': 'comparison', 'generation': 25000, 'totalSales': 9967524}]
        main()
        output = sys.stdout.getvalue().strip()
        self.assertIn('9,967,524', output)
        self.assertIn('25,000', output)
