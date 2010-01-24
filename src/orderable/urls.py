from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        regex = r'orderable.js$',
        view  = 'orderable.views.javascript',
        name  = 'javascript',
    ),
)