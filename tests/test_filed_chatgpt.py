"""Tests for filed_chatgpt."""

import sys
import unittest
from io import StringIO
from unittest.mock import patch

from filed_chatgpt.filed_chatgpt_main import get_args, main


class TestFileChatGPT(unittest.TestCase):

    def __capture_stdout(self, *args):
        with patch.object(sys, 'argv', ['filed_chatgpt_main.py'] + list(args)):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                main()
                return mock_stdout.getvalue().strip()

    def test_main_with_input(self):
        args = (['filed_chatgpt_main.py'] +
                ['-o', 'path/file', '-m', 'some_model'])
        with patch.object(sys, 'argv', args):
            out = get_args()
            expected_arg_dict = {
                'model': 'some_model',
                'output_file': 'path/file'
            }
            self.assertDictEqual(expected_arg_dict, out)


if __name__ == '__main__':
    unittest.main()
