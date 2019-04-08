Installation
============

The platform was developed for Python 3.6+ and was tested with Python 3.7.1+

Installation with PIP
---------------------

.. code-block:: bash

    pip install botx

Requirements for Bots
---------------------

To receive messages from BotX platform you need to use the WebHook method.
You need a HTTP-server with 2 reserved endpoints:

 * ``/status`` (incoming GET-requests)
 * ``/command`` (incoming POST-requests)
