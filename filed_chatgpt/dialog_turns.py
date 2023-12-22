"""Dialog turns for serializing to a YAML file."""

import yaml

from filed_chatgpt.message import Message


class DialogTurns:
    """Class for managing dialog turns and serializing them to a YAML file."""

    def __init__(self, model: str):
        """
        Initialize DialogTurns with the specified ChatGPT model.

        Args:
            model (str): The ChatGPT model to be associated with
                the dialog turns.
        """
        assert model is not None
        self.model = model
        self.dialog_turns = []

    def add_message(self, message: Message):
        """
        Add a Message object to the dialog turns.

        Args:
            message (Message): The message to be added to the dialog turns.
        """
        if message is None:
            return
        self.dialog_turns.append(message)

    def get_last_message(self) -> Message:
        """
        Retrieve the last message in the dialog turns.

         Returns:
             Message: The last message in the dialog turns.
        """
        if len(self.dialog_turns) == 0:
            return None
        return self.dialog_turns[:1][0]

    def messages(self):
        """
        Return messages in a format that can be used in the OpenAI API.

        Returns:
            list: List of dictionaries with 'role' and 'content'
                keys for each message.
        """
        return [{'role': message.role, 'content': message.content}
                for message in self.dialog_turns]

    def serialize(self, output_file: str):
        """
        Serialize the dialog turns to a YAML file.

        Args:
            output_file (str): The path to the output YAML file.
        """
        if output_file is None:
            return
        with open(output_file, 'w') as yaml_file:
            yaml.dump(self, yaml_file, indent=4)

    def __str__(self):
        """
        Return a YAML string representation of the dialog turns.

         Returns:
             str: YAML string representation of the dialog turns.
         """
        return yaml.dump(self, indent=4)
