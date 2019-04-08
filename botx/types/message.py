from typing import Any, Dict, Optional
from uuid import UUID

from pydantic import Schema

from .base import BotXType
from .core import ChatTypeEnum, SyncID
from .file import File


class MessageUser(BotXType):
    user_huid: Optional[UUID]
    group_chat_id: UUID
    chat_type: ChatTypeEnum
    ad_login: Optional[str]
    ad_domain: Optional[str]
    username: Optional[str]
    host: str


class MessageCommand(BotXType):
    body: str
    data: Dict[str, Any] = {}

    @property
    def cmd(self) -> str:
        return self.body.split(" ", 1)[0]

    @property
    def cmd_arg(self) -> str:
        return "".join(self.body.split(" ", 1)[1:])


class Message(BotXType):
    """
    A Message object, which was received from BotX

    :param SyncID sync_id: Id of the message
    """
    sync_id: SyncID
    command: MessageCommand
    file: Optional[File] = None
    user: MessageUser = Schema(..., alias="from")
    bot_id: UUID

    def __init__(self, **data):
        super().__init__(**data)

        self.sync_id = SyncID(data["sync_id"])

    @property
    def body(self) -> str:
        """
        The text of the message

        :getter: Returns the text of the message
        :type: str
        """
        return self.command.body

    @property
    def data(self) -> Dict[str, Any]:
        return self.command.data

    @property
    def user_huid(self) -> Optional[UUID]:
        """
        The user_huid of the message

        :getter: Returns the user_huid for the message
        :type: UUID
        """
        return self.user.user_huid

    @property
    def ad_login(self) -> Optional[str]:
        """
        The ad_login of the message

        :getter: Returns the ad_login for the message
        :type: str
        """
        return self.user.ad_login

    @property
    def group_chat_id(self) -> UUID:
        """
        The group_chat_id of the message

        :getter: Returns the group_chat_id of the message
        :type: UUID
        """
        return self.user.group_chat_id

    @property
    def chat_type(self) -> str:
        """
        The chat_type of the message

        :getter: Returns the chat_type of the message
        :type: str
        """
        return self.user.chat_type.name

    @property
    def host(self) -> str:
        """
        The host of the message

        :getter: Returns the host of the message
        :type: str
        """
        return self.user.host
