VENV := venv
FLASK_ARGS := --reload --host 0.0.0.0

.DEFAULT_GOAL := server
.PHONY: clean-venv server

clean-venv:
	rm -rf $(VENV)

server: $(VENV)
	@(. $(VENV)/bin/activate &&\
	export FLASK_ENV=development;\
	flask run $(FLASK_ARGS))

$(VENV):
	python3 -m venv $(VENV)
	@(. $(VENV)/bin/activate && pip install -r requirements.txt)
