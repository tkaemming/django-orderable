from django import forms
from django.contrib import admin

class OrderableAdmin(admin.ModelAdmin):
    exclude = ('order',)
    order_field = 'order'
    
    change_list_template = 'orderable/change_list.html'
    
    def __init__(self, *args, **kwargs):
        super(OrderableAdmin, self).__init__(*args, **kwargs)
        
        if self.order_field not in self.list_display:
            self.list_display = list(self.list_display) + [self.order_field]
        
        if self.order_field not in self.list_editable:
            self.list_editable = list(self.list_editable) + [self.order_field]

class OrderableInline(object):
    def _media(self):
        from django.core.urlresolvers import reverse
        return forms.Media(js=(
            'http://ajax.googleapis.com/ajax/libs/jquery/1.4.0/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.7.2/jquery-ui.min.js',
            reverse('orderable:javascript'),
        ))
    media = property(_media)

class OrderableStackedInline(OrderableInline, admin.StackedInline):
    template = 'orderable/edit_inline/stacked.html'

class OrderableTabularInline(OrderableInline, admin.TabularInline):
    template = 'orderable/edit_inline/tabular.html'