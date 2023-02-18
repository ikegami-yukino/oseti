# -*- coding: utf-8 -*-
from codecs import open
import os
import pkgutil
import re
from setuptools import setup

install_requires = [] if pkgutil.find_loader('MeCab') else ['mecab']

with open(os.path.join('oseti', '__init__.py'), 'r', encoding='utf8') as f:
    version = re.compile(r".*__version__ = '(.*?)'",
                         re.S).match(f.read()).group(1)

setup(name='oseti',
      packages=['oseti'],
      version=version,
      license='MIT License',
      platforms=['POSIX', 'Windows', 'Unix', 'MacOS'],
      description='Dictionary based Sentiment Analysis for Japanese',
      author='Yukino Ikegami',
      author_email='yknikgm@gmail.com',
      url='https://github.com/ikegami-yukino/oseti',
      keywords=['sentiment analysis'],
      classifiers=[
          'Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: Japanese',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Topic :: Text Processing :: Linguistic'
      ],
      long_description='%s\n\n%s' %
      (open('README.rst', encoding='utf8').read(),
       open('CHANGES.rst', encoding='utf8').read()),
      package_data={'oseti': ['dic/*.json']},
      install_requires=['bunkai'] + install_requires,
      tests_require=['pytest'],
      test_suite='pytest')
