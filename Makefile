black:
	black dplyr tests setup.py --check

flake:
	flake8 dplyr tests setup.py

test:
	pytest

check: black test flake

install:
	python -m pip install -e .
