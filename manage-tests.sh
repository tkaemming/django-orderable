#!/bin/sh
export PYTHONPATH="${PWD}/src:${PYTHONPATH}"
export DJANGO_SETTINGS_MODULE='orderable.tests.settings'
django-admin.py $@