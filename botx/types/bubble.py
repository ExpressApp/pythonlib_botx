from typing import Optional

from .base import BotXType


class BubbleElement(BotXType):
    """
    A Bubble is the element that is displayed as a button under the message

    :param str label: A label of the bubble
    :param str command: A command, which will be sent
    """
    command: str
    label: Optional[str] = None

    def __init__(self, **data):
        super().__init__(**data)
        self.label = self.label or self.command
