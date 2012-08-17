import posixpath
from django import forms
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage

from orderable.settings import JQUERY_URL, JQUERYUI_URL

class OrderableAdmin(admin.ModelAdmin):
    exclude = ('order',)
    order_field = 'order'
    ordering = ('order',)
    
    change_list_template = 'orderable/change_list.html'
    
    class Media:
        js = (
            JQUERY_URL,
            JQUERYUI_URL,
            staticfiles_storage.url('orderable/orderable.js')
        )
    
    def __init__(self, *args, **kwargs):
        super(OrderableAdmin, self).__init__(*args, **kwargs)
        
        if self.order_field not in self.list_display:
            self.list_display = list(self.list_display) + [self.order_field]
        
        if self.order_field not in self.list_editable:
            self.list_editable = list(self.list_editable) + [self.order_field]

class OrderableInline(object):

    class Media:
        js = (
            JQUERY_URL,
            JQUERYUI_URL,
            staticfiles_storage.url('orderable/orderable.js')
        )

class OrderableStackedInline(OrderableInline, admin.StackedInline):
    template = 'orderable/edit_inline/stacked.html'

class OrderableTabularInline(OrderableInline, admin.TabularInline):
    template = 'orderable/edit_inline/tabular.html'
