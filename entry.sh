#!/bin/bash

cp env_template .env

sed -i -e "s/{{SECRET_KEY}}/${SECRET_KEY}/g" \
	-e "s/{{DEBUG}}/${DEBUG}/g" \
	-e "s/{{LANGUAGE_CODE}}/${LANGUAGE_CODE}/g" \
	-e "s/{{TIME_ZONE}}/${TIME_ZONE}/g" \
	-e "s/{{MAIN_DATABASE_ENGINE}}/${MAIN_DATABASE_ENGINE}/g" \
	-e "s/{{MAIN_DATABASE_NAME}}/${MAIN_DATABASE_NAME}/g" \
	-e "s/{{MAIN_DATABASE_USER}}/${MAIN_DATABASE_USER}/g" \
	-e "s/{{MAIN_DATABASE_PASSWD}}/${MAIN_DATABASE_PASSWD}/g" \
	-e "s/{{MAIN_DATABASE_HOST}}/${MAIN_DATABASE_HOST}/g" \
	-e "s/{{MAIN_DATABASE_PORT}}/${MAIN_DATABASE_PORT}/g" .env
	
python -m venv venv

. venv/bin/activate

python pip install --upgrade pip

pip install -r requirements.txt
	
python manage.py runserver --noreload 0.0.0.0:8000