from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        regex = r'^$',
        view  = 'orderable.views.order_objects',
        name  = 'orderable_order_objects',
    ),
    url(
        regex = r'orderable.js$',
        view  = 'orderable.views.get_orderable_javascript',
        name  = 'orderable_javascript',
    ),
)