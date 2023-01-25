deps:
	poetry check
	poetry update
	poetry install
	poetry export --without-hashes --format=requirements.txt > requirements.txt

dev:
	python main.py
