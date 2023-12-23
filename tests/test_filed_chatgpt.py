"""Tests for filed_chatgpt."""

import sys
import unittest
from unittest.mock import patch

from filed_chatgpt.filed_chatgpt import get_args


class TestFileChatGPT(unittest.TestCase):
    """Test for main methods."""

    def test_get_args_with_input(self):
        """Test get_args."""
        args = ["filed_chatgpt_main.py"] + [
            "-o",
            "path/file",
            "-m",
            "some_model",
        ]
        with patch.object(sys, "argv", args):
            out = get_args()
            expected_arg_dict = {
                "model": "some_model",
                "output_file": "path/file",
            }
            self.assertDictEqual(expected_arg_dict, out)


if __name__ == "__main__":
    unittest.main()
