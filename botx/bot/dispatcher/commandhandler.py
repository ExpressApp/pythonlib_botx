from typing import Any, Callable, Dict, List, Optional

from botx.core import BotXObject
from botx.types import StatusCommandUIElement, StatusCommand


class CommandHandler(BotXObject):
    """
    A Class, which is used for setting up commands of the Bot

    :param str name: A name of the command (e.g. 'Start command')
    :param str command: A command (e.g. '/start')
    :param str description: A description for the command
    :param Callable func: A callable function, which will be invoked for the command
    :param bool exclude_from_status: If set, then the command will be excluded from status
    :param bool use_as_default_handler: If set, then **ANY** unhandled command will be addressed to this handler
    :param dict options:
    :param list elements:
    :param bool system_command_handler: Set True to receive files and system commands to this handler

    .. code-block:: python3

        from botx import Bot, CommandHandler

        def some_func():
            pass

        bot = Bot()
        bot.add_handler(
            CommandHandler(
                name='Start',
                command='/start',
                func=some_func,
                description='A start command'
            )
        )
    """
    name: str
    command: str
    description: str
    func: Callable
    exclude_from_status: bool = False
    use_as_default_handler: bool = False
    options: Dict[str, Any] = {}
    elements: List[StatusCommandUIElement] = []
    system_command_handler: bool = False

    def to_status_command(self) -> Optional[StatusCommand]:
        if (
            not self.exclude_from_status
            and not self.use_as_default_handler
            and not self.system_command_handler
        ):
            return StatusCommand(
                body=self.command,
                name=self.name,
                description=self.description,
                options=self.options,
                elements=self.elements,
            )

        return None
