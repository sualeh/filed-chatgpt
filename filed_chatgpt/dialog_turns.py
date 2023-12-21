"""Dialog turns for serializing to a YAML file."""

import yaml

from filed_chatgpt.message import Message


class DialogTurns:
    """Class for dialog turns."""
    def __init__(self, model: str):
        assert model is not None
        self.model = model
        self.dialog_turns = []

    def add_message(self, message: Message):
        if message is None:
            return
        self.dialog_turns.append(message)

    def get_last_message(self) -> Message:
        return self.dialog_turns[:1][0]

    def serialize(self, output_file: str):
        if output_file is None:
            return
        with open(output_file, 'w') as yaml_file:
            yaml.dump(self.__dict__, yaml_file)

    def __str__(self):
        return yaml.dump(self)
