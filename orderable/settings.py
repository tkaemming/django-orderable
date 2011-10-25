import posixpath # does sane URL path joining
from django.conf import settings

DEFAULT_ORDERING_FIELD = getattr(settings, 'DEFAULT_ORDERING_FIELD', 'order')

# TODO: Set up a wrapper to allow jQuery UI to play nicely with Django's jQuery.
JQUERY_URL = getattr(settings, 'JQUERY_URL',
    '//ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js')
JQUERYUI_URL = getattr(settings, 'JQUERYUI_URL',
    '//ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/jquery-ui.min.js')
