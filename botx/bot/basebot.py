import abc
import logging
from typing import Any, BinaryIO, Dict, List, NoReturn, Optional, TextIO, Tuple, Union
from uuid import UUID

from botx.core import BotXAPI
from botx.types import (
    CTS,
    BotCredentials,
    BubbleElement,
    KeyboardElement,
    Mention,
    Message,
    ResponseRecipientsEnum,
    Status,
    SyncID,
)

from .dispatcher.basedispatcher import BaseDispatcher
from .dispatcher.commandhandler import CommandHandler
from .router import CommandRouter

LOGGER = logging.getLogger("botx")


class BaseBot(abc.ABC, CommandRouter):
    _dispatcher: BaseDispatcher
    _credentials: BotCredentials
    _disable_credentials: bool
    _url_token: str = BotXAPI.V2.token.url
    _url_command: str = BotXAPI.V3.command.url
    _url_notification: str = BotXAPI.V3.notification.url
    _url_file: str = BotXAPI.V1.file.url

    def __init__(
        self,
        *,
        credentials: Optional[BotCredentials] = None,
        disable_credentials: bool = False,
    ):
        super().__init__()

        self._credentials = credentials if credentials else BotCredentials()

        if disable_credentials:
            LOGGER.warning("token obtaining disabled")

        self._disable_credentials = disable_credentials

    def register_cts(self, cts: CTS):
        LOGGER.debug(f"register new CTS {cts.host !r} for bot")

        self._credentials.known_cts[cts.host] = (cts, None)

    def add_cts_credentials(self, credentials: BotCredentials) -> NoReturn:
        LOGGER.debug(f"add new credentials for bot {credentials.json() !r}")
        self._credentials.known_cts.update(credentials.known_cts)

    def get_cts_credentials(self) -> BotCredentials:
        return self._credentials

    def add_handler(self, handler: CommandHandler) -> NoReturn:
        """
        A method that is used to add recognizable commands to Bot

        :param CommandHandler handler: A CommandHandler object
        """
        self._dispatcher.add_handler(handler)

    def add_commands(self, router: CommandRouter) -> NoReturn:
        for _, handler in router._handlers.items():
            self.add_handler(handler)

    def _get_token_from_credentials(self, host) -> Optional[str]:
        credentials = self._credentials.known_cts.get(host, (None, None))[1]
        if not credentials:
            LOGGER.debug(f"no credentials for {host !r} found")
            return None

        return credentials.result

    def start(self) -> NoReturn:
        """Run some outer dependencies that can not be started in init"""

    @abc.abstractmethod
    def stop(self) -> NoReturn:
        """Stop special objects and dispatcher for bot"""

    @abc.abstractmethod
    def parse_status(self) -> Status:
        """Create status object for bot"""

    @abc.abstractmethod
    def parse_command(self, data: Dict[str, Any]) -> bool:  # pragma: no cover
        """Execute command from request"""

    @abc.abstractmethod
    def _obtain_token(self, host: str, bot_id: UUID) -> Tuple[str, int]:
        """Obtain token from BotX for making requests"""

    @abc.abstractmethod
    def send_message(
        self,
        text: str,
        chat_id: Union[SyncID, UUID, List[UUID]],
        bot_id: UUID,
        host: str,
        *,
        file: Optional[Union[TextIO, BinaryIO]] = None,
        recipients: Union[List[UUID], str] = ResponseRecipientsEnum.all,
        mentions: Optional[List[Mention]] = None,
        bubble: Optional[List[List[BubbleElement]]] = None,
        keyboard: Optional[List[List[KeyboardElement]]] = None,
    ) -> Tuple[str, int]:
        """Create answer for notification or for command and send it to BotX API"""

    @abc.abstractmethod
    def answer_message(
        self,
        text: str,
        message: Message,
        *,
        file: Optional[Union[TextIO, BinaryIO]] = None,
        recipients: Union[List[UUID], str] = ResponseRecipientsEnum.all,
        mentions: Optional[List[Mention]] = None,
        bubble: Optional[List[List[BubbleElement]]] = None,
        keyboard: Optional[List[List[KeyboardElement]]] = None,
    ):
        """Send message with credentials from incoming message"""

    @abc.abstractmethod
    def _send_command_result(
        self,
        text: str,
        chat_id: SyncID,
        bot_id: UUID,
        host: str,
        file: Optional[Union[TextIO, BinaryIO]],
        recipients: Union[List[UUID], str],
        mentions: List[Mention],
        bubble: List[List[BubbleElement]],
        keyboard: List[List[KeyboardElement]],
    ) -> Tuple[str, int]:
        """Send command result answer"""

    @abc.abstractmethod
    def _send_notification_result(
        self,
        text: str,
        group_chat_ids: List[UUID],
        bot_id: UUID,
        host: str,
        file: Optional[Union[TextIO, BinaryIO]],
        recipients: Union[List[UUID], str],
        mentions: List[Mention],
        bubble: List[List[BubbleElement]],
        keyboard: List[List[KeyboardElement]],
    ) -> Tuple[str, int]:
        """Send notification result answer"""

    @abc.abstractmethod
    def send_file(
        self,
        file: Union[TextIO, BinaryIO],
        chat_id: Union[SyncID, UUID],
        bot_id: UUID,
        host: str,
    ) -> Tuple[str, int]:
        """Send separate file to BotX API"""
