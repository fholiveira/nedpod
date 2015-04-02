ACTIVE_VENV=. ../.ned/bin/activate

all: unit integration
.PHONY: all


.PHONY: unit
unit: 
	@echo "UNIT TESTS"
	@$(ACTIVE_VENV) && nosetests --with-yanc --with-xunit unit/
	@echo -e "\n"

.PHONY: integration
integration: 
	@echo "INTEGRATION TESTS"
	@$(ACTIVE_VENV) && nosetests --with-yanc --with-xunit integration/
