# Define variables
PYTHON_VERSION = 3.8
VENV_DIR = .venv

# Define targets
.PHONY: all setup install test clean ci

all: setup install test

setup:
	python3 -m venv $(VENV_DIR)
	. $(VENV_DIR)/bin/activate && pip install --upgrade pip

install:
	. $(VENV_DIR)/bin/activate && pip install -r $(PWD)/plsql_to_pyspark/requirements.txt

test:
	PYTHONPATH=$(PWD)/plsql_to_pyspark/src . $(VENV_DIR)/bin/activate && echo "PYTHONPATH is: $${PYTHONPATH}" && pytest plsql_to_pyspark/src/test/pyspark/

clean:
	rm -rf $(VENV_DIR)
	find . -type d -name "__pycache__" -exec rm -rf {} +

ci:
	act -W plsql_to_pyspark/.github/workflows/ci.yml
