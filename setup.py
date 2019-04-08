# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['botx', 'botx.bot', 'botx.bot.dispatcher', 'botx.types']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.5,<4.0',
 'aiojobs>=0.2.2,<0.3.0',
 'pydantic>=0.20.1,<0.21.0',
 'requests>=2.21,<3.0']

setup_kwargs = {
    'name': 'botx',
    'version': '0.9.3',
    'description': 'Python implementation for Express BotX API',
    'long_description': None,
    'author': 'Michael Morozov',
    'author_email': 'mmorozov@ccsteam.ru',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
