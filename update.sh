#!/bin/bash

poetry run pre-commit run -a
poetry run pytest

poetry run git add . && poetry run git commit -m "format & fix"

poetry run bumpversion parch
