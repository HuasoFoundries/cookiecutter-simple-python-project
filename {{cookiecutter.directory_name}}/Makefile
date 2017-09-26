SHELL := /usr/bin/env bash

.PHONY: clean-pyc
.PHONY: install, requirements, lint
.PHONY: install-deps-apt

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

env:
	python3 -m venv ./env

lint:
	flake8 src/

## Install Python dependencies
requirements:
	pip install --upgrade pip
	pip install -r requirements.txt

# Install Apt dependencies
install-deps-apt:
	apt-get install $$(cat AptFile | sed 's/#.*$$//')