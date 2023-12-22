"""Class for one message that is either a prompt or a completion."""
import uuid

import yaml
from openai.types.chat.chat_completion import ChatCompletion


class Message:
    """
    Class representing a message.

    The message can be either a user prompt or an AI completion.
    """

    @staticmethod
    def from_prompt(content: str, role: str = 'user'):
        """Creates a Message instance from a user prompt.

        Args:
            content (str): The text of the user prompt.
            role (str, optional): The role of the message. Defaults to 'user'.

        Returns:
            Message: The created Message instance.
        """
        return Message('chatprmt-' + uuid.uuid4().__str__(), role, content)

    @staticmethod
    def from_completion(completion: ChatCompletion):
        """Creates a Message instance from an AI completion.

        Args:
            completion (ChatCompletion): The completion object from
                the OpenAI API.

        Returns:
            Message: The created Message instance.
        """
        message = completion.choices[0].message
        return Message(completion.id, message.role, message.content)

    def __init__(self, message_id: str, role: str, content: str):
        """Initialize a Message instance with the specified attributes.

        Args:
            message_id (str): Unique identifier for the message.
            role (str): The role of the message.
            content (str): The content of the message.
        """
        self.message_id = message_id
        self.role = role
        self.content = content

    def role(self) -> str:
        """Returns the role of the user.

        Returns:
            str: The role of the user.
        """
        return self.role

    def content(self) -> str:
        """Returns the content of the message.

        Returns:
            str: The content of the message.
        """
        return self.content()

    def message_id(self) -> str:
        """Returns the unique identifier of the message.

        Returns:
            str: The unique identifier of the message.
        """
        return self.message_id

    def __eq__(self, other) -> bool:
        """Checks if two Message instances are equal.

        Args:
            other (Message): Another Message instance.

        Returns:
            bool: True if the two instances are equal, False otherwise.
        """
        if other is None:
            return False
        if not isinstance(other, Message):
            return False
        return (self.role, self.content) == (other.role, other.content)

    def __str__(self) -> str:
        """Returns a YAML string representation of the message.

        Returns:
            str: YAML string representation of the message.
        """
        return yaml.dump(self, indent=4)
