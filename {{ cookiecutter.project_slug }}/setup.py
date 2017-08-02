#!/usr/bin/env python

from distutils.core import setup

setup(
    name='{{ cookiecutter.project_slug }}',
    version='0.1dev',
    description='This is https://github.com/mozilla/{{ cookiecutter.project_slug }}',
    author='Mozilla Foundation',
    author_email='',
    url='https://github.com/mozilla/{{ cookiecutter.project_slug }}'
)
