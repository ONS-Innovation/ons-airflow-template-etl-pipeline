# Makefile for ETL Pipeline Project

# Define Python and other variables
PYTHON=python3
PIP=pip
TEST_DIR=tests
UNIT_TESTS=$(TEST_DIR)/unit
E2E_TESTS=$(TEST_DIR)/e2e

# Define commands
install:
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt

lint:
	flake8 etl

test:
	PYTHONPATH=. pytest $(UNIT_TESTS)
	PYTHONPATH=. pytest $(E2E_TESTS)

run:
	$(PYTHON) scripts/run_etl.py

docker-build:
	docker build -t etl-pipeline .

docker-run:
	docker run --rm etl-pipeline

security:
	bandit -r etl

.PHONY: install lint test run docker-build docker-run
