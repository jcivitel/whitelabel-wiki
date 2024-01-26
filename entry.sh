#!/bin/bash

cp env_template .env

sed -i -e "s/{{SECRET_KEY}}/${SECRET_KEY}/g" ".env"
sed -i -e "s/{{DEBUG}}/${DEBUG}/g" ".env"
sed -i -e "s/{{LANGUAGE_CODE}}/${LANGUAGE_CODE}/g" ".env"
sed -i -e "s/{{TIME_ZONE}}/${TIME_ZONE}/g" ".env"
sed -i -e "s/{{MAIN_DATABASE_ENGINE}}/${MAIN_DATABASE_ENGINE}/g" ".env"
sed -i -e "s/{{MAIN_DATABASE_NAME}}/${MAIN_DATABASE_NAME}/g" ".env"
sed -i -e "s/{{MAIN_DATABASE_USER}}/${MAIN_DATABASE_USER}/g" ".env"
sed -i -e "s/{{MAIN_DATABASE_PASSWD}}/${MAIN_DATABASE_PASSWD}/g" ".env"
sed -i -e "s/{{MAIN_DATABASE_HOST}}/${MAIN_DATABASE_HOST}/g" ".env"
sed -i -e "s/{{MAIN_DATABASE_PORT}}/${MAIN_DATABASE_PORT}/g" ".env"

python -m venv venv

python pip install --upgrade pip

. venv/bin/activate

pip install -r requirements.txt

python manage.py runserver --noreload 0.0.0.0:8000