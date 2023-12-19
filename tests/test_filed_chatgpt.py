"""Tests for filed_chatgpt."""

import sys
import unittest
from io import StringIO
from unittest.mock import patch

from filed_chatgpt.filed_chatgpt import main


class TestFileChatGPT(unittest.TestCase):

    def assert_stdout(self, expected_output, *args):
        with patch.object(sys, 'argv', ['filed_chatgpt.py'] + list(args)):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                main()
                self.assertEqual(
                    mock_stdout.getvalue().strip(),
                    expected_output
                )

    def test_main_with_input(self):
        self.assert_stdout("['hello,', 'world']", 'hello,', 'world')

    def test_main_without_input(self):
        self.assert_stdout('[]')
