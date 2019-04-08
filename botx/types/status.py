from typing import List

from .base import BotXType
from .core import StatusCommand, StatusEnum


class StatusResult(BotXType):
    enabled: bool = True
    status_message: str = "Bot is working"
    commands: List[StatusCommand] = []


class Status(BotXType):
    status: StatusEnum = StatusEnum.ok
    result: StatusResult = StatusResult()
