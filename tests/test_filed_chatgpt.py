"""Tests for filed_chatgpt."""

import sys
import unittest
from io import StringIO
from unittest.mock import patch

from filed_chatgpt.filed_chatgpt import main


class TestFileChatGPT(unittest.TestCase):

    def capture_stdout(self, *args):
        with patch.object(sys, 'argv', ['filed_chatgpt.py'] + list(args)):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                main()
                return mock_stdout.getvalue().strip()


    def test_main_with_input(self):
        out = self.capture_stdout('-o', 'file', '-k', 'apikey123')
        self.assertEqual(
            out,
            "Namespace(model='gpt-3.5-turbo', api_key='apikey123', output_file='file')"
        )
