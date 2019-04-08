from typing import Optional

from .base import BotXType


class KeyboardElement(BotXType):
    """
    A KeyboardElement is the element that is displayed in the keyboard under
    the chat

    :param str label: A label of the keyboard element
    :param str command: A command, which will be sent
    """
    command: str
    label: Optional[str] = None

    def __init__(self, **data):
        super().__init__(**data)
        self.label = self.label or self.command
