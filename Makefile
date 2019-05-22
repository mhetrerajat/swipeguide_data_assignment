# Makefile for common commands

PYTHON=pipenv run python
PROJECT_HOME?=.

.DEFAULT: help

help:
	@echo "make test - To run test cases"
	@echo "make pretty - Does linting and deletes *.pyc files"
	@echo "make requirements - Makes requirements.txt"
	@echo "make report - Generates code coverage report"
pretty:
	find . -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	isort -rc --atomic $(PROJECT_HOME)
	find . -type f -name "*.py" -exec $(PYTHON) -m yapf --recursive --parallel --in-place --verbose --style=pep8 {} \;
	find . -type f -name "*.py" -exec $(PYTHON) -m autoflake --recursive --in-place --remove-unused-variables --remove-all-unused-imports --exclude=__init__.py {} \;

test:
	$(PYTHON) -m unittest

requirements:
	$(PYTHON) -m pip freeze > requirements.txt

report:
	$(PYTHON) -m coverage run --include=app/* --omit=tests/*,config.py -m unittest discover --start-directory=tests
	$(PYTHON) -m coverage report 
	$(PYTHON) -m coverage html
	rm -rf coverage.svg
	coverage-badge -o coverage.svg
	open htmlcov/index.html
