from django.conf.urls.defaults import *
from django.contrib.admin import autodiscover, site

autodiscover()

urlpatterns = patterns('',
    url(
        regex = r'^admin/',
        view  = include(site.urls),
    ),
    url(
        regex = r'^admin/orderable/',
        view  = include('orderable.urls', namespace='orderable'),
    ),
)