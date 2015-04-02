REQUIREMENTS_DEV=requirements-dev.txt
REQUIREMENTS=requirements.txt
PYTHON=python3.4
VENV=.ned

ACTIVE_VENV=. $(VENV)/bin/activate

all: run

run: 
	@$(ACTIVE_VENV) && $(PYTHON) src/app.py

test:
	@cd tests && $(MAKE)

configure: 
	@rm -rf $(VENV)
	@$(PYTHON) -m venv $(VENV)

	@$(ACTIVE_VENV) && pip install -r $(REQUIREMENTS_DEV)
	@$(ACTIVE_VENV) && pip install -r $(REQUIREMENTS)

deps:
	@$(ACTIVE_VENV) && pip freeze > $(REQUIREMENTS)
