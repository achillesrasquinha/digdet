.PHONY: build

PYTHON = python

install:
	cat requirements/*.txt > requirements.txt

	pip install -r requirements.txt

	bundle install

	npm install .

start:
	fuser -k 5000/tcp

	$(PYTHON) run.py & npm start

clean:
	find . | grep -E "__pycache__" | xargs rm -rf

	rm -rf .sass-cache

	clear

all:
	make clean install start

make push:
	git push origin master & git push heroku master
