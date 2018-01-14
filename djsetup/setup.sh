#!/usr/bin/env sh

mkdir -p "$2" > /dev/null
cd "$2"
virtualenv env
. env/bin/activate
pip install django django_extensions
django-admin startproject "$1" .
pip freeze > requirements.txt