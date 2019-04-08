Reference
=========

.. contents::
    :depth: 3
    :local:

Bots
----

BaseBot
~~~~~~~

.. module:: botx.bot.basebot
.. autoclass:: BaseBot

    .. automethod:: add_handler

SyncBot
~~~~~~~

.. module:: botx.bot.syncbot
.. autoclass:: SyncBot
    :show-inheritance:

    .. automethod:: start
    .. automethod:: stop
    .. automethod:: parse_status
    .. automethod:: parse_command
    .. automethod:: send_message
    .. automethod:: send_file

AsyncBot
~~~~~~~~

.. module:: botx.bot.asyncbot
.. autoclass:: AsyncBot
    :show-inheritance:

    .. automethod:: start
    .. automethod:: stop
    .. automethod:: parse_status
    .. automethod:: parse_command
    .. automethod:: send_message
    .. automethod:: send_file

CommandHandler
--------------

.. module:: botx.bot.dispatcher.commandhandler
.. autoclass:: CommandHandler

.. seealso:: The another way to handle bot's commands is to use a
    ``@bot.command`` decorator :meth:`botx.bot.router.CommandRouter.command`

CommandRouter
-------------

.. module:: botx.bot.router
.. autoclass:: CommandRouter

    .. automethod:: command

Message
-------

.. module:: botx.types.message
.. autoclass:: Message
    :members:

File
----

.. module:: botx.types.file
.. autoclass:: File
    :members:

BubbleElement
-------------

.. module:: botx.types.bubble
.. autoclass:: BubbleElement
    :members:
    :show-inheritance:

KeyboardElement
---------------

.. module:: botx.types.keyboard
.. autoclass:: KeyboardElement
    :members:
    :show-inheritance:
