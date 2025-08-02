# -*- coding: utf-8 -*-
from codecs import open
import importlib.util
import os
import re
from setuptools import setup

install_requires = [] if importlib.util.find_spec('MeCab') else ['mecab']

with open(os.path.join('oseti', '__init__.py'), 'r', encoding='utf8') as f:
    version = re.compile(r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1) # type: ignore


setup(name='oseti',
    packages=['oseti'],
    version=version,
    install_requires=['bunkai'] + install_requires,
    tests_require=['pytest'],
    test_suite='pytest'
)
