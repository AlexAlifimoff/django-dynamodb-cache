#!/usr/bin/env python
# pylint: disable=missing-docstring,invalid-name

import sys
from setuptools import setup, find_packages

with open('README.rst') as file:
    long_description = file.read()

config = {
    'name' : 'django-django-cache',
    'version' : '0.0.1',
    'packages' : find_packages(),
    'author' : 'Alex Alifimoff',
    'author_email' : 'alex@sixteenzero.net',
    'license' : 'BSD',
    'description' : 'Amazon DynamoDB cache backend for Django',
    'long_description' : long_description,
    'url' : 'https://github.com/AlexAlifimmoff/django-dynamocdb-cache',
    'keywords' : ['Amazon', 'DynamoDB', 'Django', 'cache'],
    'zip_safe' : False,
    'install_requires' : ['boto', 'django-storages>=1.1.8', 'Django'],
}

if (len(sys.argv) >= 2) and (sys.argv[1] == '--requires'):
    for req in config['install_requires']:
        print(req)
else:
    setup(**config)
