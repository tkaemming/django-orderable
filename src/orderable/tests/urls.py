from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.admin import autodiscover, site

autodiscover()

urlpatterns = patterns('',
    url(
        regex = r'^admin/',
        view  = include(site.urls),
    ),
    url(
        regex  = r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], 
        view   = 'django.views.static.serve', 
        kwargs = {'document_root': settings.STATIC_URL}
    ),
)