#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name = 'django-orderable',
    version = '1.2',
    description = 'Model ordering for the Django administration site.',
    
    author = 'Ted Kaemming',
    author_email = 'ted@kaemming.com',
    url = 'http://www.github.com/tkaemming/django-orderable/',
    
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    package_data = {
        'orderable': [
            'templates/orderable/change_list.html',
            'templates/orderable/edit_inline/stacked.html',
            'templates/orderable/edit_inline/tabular.html',
            'media/orderable/orderable.js',
            'locale/*/LC_MESSAGES/django.*',
        ]
    },
    
    install_requires = ['setuptools'],
    zip_safe = False
)