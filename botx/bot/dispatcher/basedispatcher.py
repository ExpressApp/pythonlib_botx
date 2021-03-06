import abc
import inspect
import logging
from collections import OrderedDict
from typing import Any, Awaitable, Dict, NoReturn, Optional, Union

from botx.core import BotXException
from botx.types import RequestTypeEnum, Status, StatusResult

from .commandhandler import CommandHandler

LOGGER = logging.getLogger("botx")


class BaseDispatcher(abc.ABC):
    _handlers: Dict[str, CommandHandler]
    _default_handler: Optional[CommandHandler] = None
    _bot: "BaseBot"

    def __init__(self, bot):
        self._handlers = OrderedDict()
        self._bot = bot

    def start(self) -> NoReturn:
        """Start dispatcher-related things like aiojobs.Scheduler"""

    @abc.abstractmethod
    def shutdown(self) -> NoReturn:
        """Stop dispatcher-related things like thread or coroutine joining"""

    @abc.abstractmethod
    def parse_request(
        self, data: Dict[str, Any], request_type: Union[str, RequestTypeEnum]
    ) -> Union[Status, bool]:
        """Parse request and call status creation or executing handler for command"""

    @abc.abstractmethod
    def _create_message(self, data: Dict[str, Any]) -> Union[Awaitable, bool]:
        """Create new message for command handler and spawn worker for it"""

    def _create_status(self) -> Status:
        commands = []
        for command_name, handler in self._handlers.items():
            menu_command = handler.to_status_command()
            if menu_command:
                commands.append(menu_command)

        return Status(result=StatusResult(commands=commands))

    def add_handler(self, handler: CommandHandler) -> NoReturn:
        if len(inspect.getfullargspec(handler.func).args) != 2:
            raise BotXException(
                "command handler for bot requires 2 arguments for message and for bot instance"
            )

        if handler.use_as_default_handler:
            LOGGER.debug(f"set default handler {handler.name !r}")
            self._default_handler = handler
        else:
            LOGGER.debug(f"add new handler for {handler.command !r}")
            self._handlers[handler.command] = handler
