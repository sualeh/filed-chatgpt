# test_myscript.py

import unittest
from unittest.mock import patch
from io import StringIO
import sys
import filed_chatgpt

class TestFileChatGPT(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout, *args):
        with patch.object(sys, 'argv', ['filed_chatgpt.py'] + list(args)):
            filed_chatgpt.main()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_main_with_input(self):
        self.assert_stdout("hello, world", 'hello,', 'world')

    def test_main_without_input(self):
        self.assert_stdout("[]")
