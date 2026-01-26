import unittest
import sys
from io import StringIO
from command_line import main

class TestCommandLine(unittest.TestCase):
    def test_normal_query(self):
        """test a valid state in the command line interface"""
