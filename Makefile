black:
	black dplyr tests setup.py

flake:
	flake8 dplyr tests setup.py

test:
	pytest

check: black test flake

pre-commit:
	pre-commit run --all-files

install:
	python -m pip install -e .

install-dev: install
	python -m pip install -e ".[dev]"
	pre-commit install

install-test: install
	python -m pip install -e ".[test]"

clean:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ .ipynb_checkpoints .pytest_cache
