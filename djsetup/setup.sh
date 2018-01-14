#!/usr/bin/env sh

virtualenv env
. env/bin/activate
pip install django django_extensions
mkdir -p "$2" > /dev/null
django-admin startproject "$1" "$2"
pip freeze > requirements.txt