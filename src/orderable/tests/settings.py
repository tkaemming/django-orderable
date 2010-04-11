import os

TEST_PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
ORDERABLE_ROOT = os.path.join(TEST_PROJECT_ROOT, '..')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(TEST_PROJECT_ROOT, 'test.db')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'orderable',
    'orderable.tests',
)

ROOT_URLCONF = 'orderable.tests.urls'

MEDIA_ROOT = os.path.join(ORDERABLE_ROOT, 'media')
MEDIA_URL = '/static/'