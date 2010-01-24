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

class OrderableStackedInline(admin.StackedInline):
    pass

class OrderableTabularInline(admin.TabularInline):
    pass