from django.contrib import admin

class OrderableAdmin(admin.ModelAdmin):
    change_list_template = 'orderable/change_list.html'
    
    def __init__(self, *args, **kwargs):
        """
        Adds the 'order_field' to the ModelAdmin list_display for this model.
        """
        super(OrderableAdmin, self).__init__(*args, **kwargs)
        self.list_display = list(self.list_display) + ('order_field',)
    
    def get_fieldsets(self, *args, **kwargs):
        """
        Removes the "order" field from display on the model's add and change views.
        """
        fieldsets = super(OrderableAdmin, self).get_fieldsets(*args, **kwargs)
        
        # Remove the "order" field from any of the fieldsets in the form.
        for fieldset in fieldsets:
            options = fieldset[1]
            fields = list(options['fields'])
            if 'order' in fields:
                index = fields.index('order')
                fields.pop(index)
                options['fields'] = fields
        
        return fieldsets
        
    def order_field(self, obj):
        """
        Creates an "order" field for use in the the change list display.
        
        This field is used as a JavaScript hook for the jQuery Sortable plugin,
        allowing arbitrary on-the-fly ordering of objects in the admin change_list
        view.
        """
        return '<input type="text" name="order-%s" value="%s" class="ordering" />' % (obj.id, obj.order or 0)
    order_field.allow_tags = True