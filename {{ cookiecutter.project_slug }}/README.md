{{ cookiecutter.project_name }}
===========================

[![CircleCI](https://img.shields.io/circleci/project/github/mozilla/{{ cookiecutter.project_slug }}/master.svg)](https://circleci.com/gh/mozilla/{{ cookiecutter.project_slug }})
[![codecov](https://codecov.io/gh/mozilla/{{ cookiecutter.project_slug }}/branch/master/graph/badge.svg)](https://codecov.io/gh/mozilla/{{ cookiecutter.project_slug }})

{{ cookiecutter.project_short_description }}


Instructions for development
----------------------------

0. Make sure you have [docker](https://docker.io) and [docker-compose](https://github.com/docker/compose)
1. make up

Instructions for deployment
---------------------------

The target environment for this project follows the [dockerflow](https://github.com/mozilla-services/Dockerflow) conventions.
In order to run it correctly, a number of environment variables needs to be set up.
The full list of variables can be found in the web section of the docker-compose.yml file.
From a services standpoint, this project requires:
 - a Postgres db to store the application data, defined by DATABASE_URL
 - an optional Redis cache service, defined by CACHE_URL
