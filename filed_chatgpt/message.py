"""Class for one message that is either a prompt or a completion."""
import uuid

import yaml
from openai.types.chat.chat_completion import ChatCompletion


class Message:
    """Class for one message."""

    @staticmethod
    def from_prompt(content: str, role: str = 'user'):
        return Message('chatprmt-' + uuid.uuid4().__str__(), role, content)

    @staticmethod
    def from_completion(completion: ChatCompletion):
        message = completion.choices[0].message
        return Message(completion.id, message.role, message.content)

    def __init__(self, id: str, role: str, content: str):
        self.message_id = id
        self.role = role
        self.content = content

    def role(self) -> str:
        return self.role

    def content(self) -> str:
        return self.content()

    def message_id(self) -> str:
        return self.message_id

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if not isinstance(other, Message):
            return False
        return (self.role, self.content) == (other.role, other.content)

    def __str__(self) -> str:
        return yaml.dump(self, indent=4)
