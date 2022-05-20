import unittest
from unittest.mock import patch
from io import StringIO
from institute import Institute
from main import *
from console import main


class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['Филиппов Петр Петрович', '172544'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_output, mock_input):
        main(['', 'add', 'student'],)
        self.assertEqual(mock_output.getvalue(),
                         'Student(code=172544, fio=\'Филиппов Петр Петрович\')\n')

    @patch('builtins.input', side_effect=['ФИИТ'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_output, mock_input):
        main(['', 'add', 'spec'],)
        self.assertEqual(mock_output.getvalue(),
                         'Specialization(name=\'ФИИТ\')\n')

    @patch('builtins.input', side_effect=['ИВТ'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_output, mock_input):
        main(['', 'get', 'spec'],)
        self.assertEqual(mock_output.getvalue(),
                         'Specialization(name=\'ИВТ\')\n')
        
    @patch('builtins.input', side_effect=[123456])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4(self, mock_output, mock_input):
        main(['', 'get', 'student'],)
        self.assertEqual(mock_output.getvalue(),
                         'Student(code=123456, fio=\'Филиппов Петр Петрович\')\n')

if __name__ == '__main__':
    unittest.main()