.PHONY: install virtualenv

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@.venv/bin/python -m venv .venv'

ipython:
	@.venv/bin/ipython

test:
	@.venv/bin/pytest -s

watch:
	# @.venv/bin/ptw -- -vv -s tests/
	@ls **/*.py | entr pytest
