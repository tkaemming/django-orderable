#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name = 'django-orderable',
    version = '1.0',
    description = 'Model ordering for the Django administration site.',
    
    author = 'Ted Kaemming',
    author_email = 'ted@kaemming.com',
    url = 'http://www.github.com/tkaemming/django-orderable/',
    
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    
    install_requires = ['setuptools']
)