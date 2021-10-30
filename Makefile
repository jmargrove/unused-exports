activate:
	ls venv/bin
	source venv/bin/activate


test:
	pytest tests

packages:
	pip freeze > requirements.txt

dev:
	nodemon --exec "python3" main.py