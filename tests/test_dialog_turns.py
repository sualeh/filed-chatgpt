import unittest

from filed_chatgpt.dialog_turns import DialogTurns
from filed_chatgpt.message import Message


class TestDialogTurns(unittest.TestCase):
    """Test dialog turns class."""

    def test_dialog_turns(self):
        """Test dialog turns class."""
        dialog_turns = DialogTurns('model')
        dialog_turns.add_message(Message.from_prompt('Hello world!'))
        message = dialog_turns.get_last_message()
        self.assertEqual(message, Message.from_prompt('Hello world!'))


if __name__ == '__main__':
    unittest.main()
