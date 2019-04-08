Examples
========

1. Example of the simple Async Bot with FastAPI
-----------------------------------------------

This is the example of the simple Async Bot that will send back arguments
from ``/echo`` command.

1.1 Create and activate virtualenv for project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate

1.2 Install dependencies
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    pip install botx fastapi uvicorn

1.3 Create ``main.py``
~~~~~~~~~~~~~~~~~~~~~~

``main.py`` file:

.. code-block:: python3

    from typing import Dict, Any
    from fastapi import FastAPI
    from botx import AsyncBot, Status

    bot = AsyncBot()

    @bot.command
    async def echo(message: Message, bot: AsyncBot):
        await bot.answer_message(message.command.cmd_arg, message)

    app = FastAPI()

    @app.get('/status', response_model=Status)
    async def status():
        return await bot.parse_status()

    @app.post('/command')
    async def command(data: Dict[str, Any]):
        return await bot.parse_command(data)

    @app.on_event('startup')
    async def on_startup():
        await bot.start()

    @app.on_event('shutdown')
    async def on_shutdown():
        await bot.stop()

1.4 Start the Bot
~~~~~~~~~~~~~~~~~

.. code-block:: bash

    uvicorn main:app --reload