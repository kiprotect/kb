SITE = "src/site.yml"
SHELL := /bin/bash

all:	site

export PATH := $(PATH):$(HOME)/.local/bin

setup: virtualenv requirements

virtualenv:
	virtualenv --python python3 venv

requirements:
	venv/bin/pip install -r requirements.txt
	npm ci

sass:
	node_modules/.bin/node-sass src/assets/scss/main.scss src/static/css/main.css

babel:
	node_modules/.bin/babel src/**/*.es6 --out-dir "."

site: sass #babel
	venv/bin/beam -vv up --site $(SITE)

clean:
	rm -rf build/*

serve:
	python3 -m http.server -d build 8111

watch: site
	./watch.sh


