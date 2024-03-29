.PHONY: venv help

venv:  ## Create a virtualenv for the app
	rm -rf venv && python -m venv venv && source venv/bin/activate && pip install setuptools

activate: ## Activate the virtualenv
	source venv/bin/activate

install:  ## Install requirements for entire app
	python setup.py install

test: ## Integration test for warrior app
	source venv/bin/activate && cd warrior && python -m pytest

help: ## Print this message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
