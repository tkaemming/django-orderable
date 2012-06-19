import posixpath # does sane URL path joining
from django.conf import settings

def is_valid(url):
    return (('://' in url) or (url.startswith('/')))

JQUERY_URL = getattr(settings, 'JQUERY_URL',
    'http://ajax.googleapis.com/ajax/libs/jquery/1.4/jquery.min.js')

if not is_valid(JQUERY_URL):
    JQUERY_URL = posixpath.join(settings.STATIC_URL, JQUERY_URL)

JQUERYUI_URL = getattr(settings, 'JQUERYUI_URL',
    'http://ajax.googleapis.com/ajax/libs/jqueryui/1.7/jquery-ui.min.js')

if not is_valid(JQUERYUI_URL):
    JQUERYUI_URL = posixpath.join(settings.STATIC_URL, JQUERYUI_URL)

ORDERABLE_STATIC_URL = getattr(settings, 'ORDERABLE_STATIC_URL',
    settings.STATIC_URL)
