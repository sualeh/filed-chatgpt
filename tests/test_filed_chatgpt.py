"""Tests for filed_chatgpt."""

import sys
import unittest
from io import StringIO
from unittest.mock import patch

from filed_chatgpt.filed_chatgpt import get_args, main


class TestFileChatGPT(unittest.TestCase):

    def __capture_stdout(self, *args):
        with patch.object(sys, 'argv', ['filed_chatgpt.py'] + list(args)):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                main()
                return mock_stdout.getvalue().strip()

    def test_main_with_input(self):
        args = ['filed_chatgpt.py'] + ['-o', 'path/file', '-m', 'somemodel']
        with patch.object(sys, 'argv', args):
            out = get_args()
            expected_arg_dict = {
                'model': 'somemodel',
                'output_file': 'path/file'
            }
            self.assertDictEqual(expected_arg_dict, out)
