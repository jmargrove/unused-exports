activate:
	ls venv/bin
	source venv/bin/activate


test:
	pytest tests

packages:
	pip freeze > requirements.txt