.PHONY: init run lint
.DEFAULT_GOAL := help

NAMESPACE := tomdewildt
NAME := google-foobar

export PYTHONPATH=src

help: ## Show this help
	@echo "${NAMESPACE}/${NAME}"
	@echo
	@fgrep -h "##" $(MAKEFILE_LIST) | \
	fgrep -v fgrep | sed -e 's/## */##/' | column -t -s##

##

init: ## Initialize the environment
	for f in requirements/*.txt; do \
		pip install -r "$$f"; \
	done

##

run: ## Run the challenge
	python src/google_foobar/${challenge}_*.py

##

lint: ## Run lint
	pylint src/google_foobar
