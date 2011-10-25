from django.contrib import admin
from orderable import settings

class OrderableModelAdmin(admin.ModelAdmin):
    change_list_template = 'orderable/change_list.html'
    ordering_field = None

    def __init__(self, *args, **kwargs):
        super(OrderableModelAdmin, self).__init__(*args, **kwargs)

        if self.ordering_field is None:
            self.ordering_field = getattr(self.model._default_manager,
                '_ordering_field', settings.DEFAULT_ORDERING_FIELD)

        if self.ordering_field not in self.list_display:
            self.list_display = list(self.list_display) + [self.ordering_field]

        if self.ordering_field not in self.list_editable:
            self.list_editable = list(self.list_editable) + [self.ordering_field]

        if self.exclude:
            self.exclude = list(self.ordering_field) + [self.ordering_field]
        else:
            self.exclude = (self.ordering_field,)

        # TODO: If the user has already specified an ordering, throw a warning
        # to let them know that we are going to override it.
        self.ordering = (self.ordering_field,)

    def changelist_view(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}

        extra_context.update({
            'ordering_field': self.ordering_field,
        })

        return super(OrderableModelAdmin, self).changelist_view(request, extra_context)

    class Media:
        js = (settings.JQUERY_URL, settings.JQUERYUI_URL, 'orderable/orderable.js')

class OrderableInline(object):
    class Media:
        js = (settings.JQUERY_URL, settings.JQUERYUI_URL, 'orderable/orderable.js')

class OrderableStackedInline(OrderableInline, admin.StackedInline):
    template = 'orderable/edit_inline/stacked.html'

class OrderableTabularInline(OrderableInline, admin.TabularInline):
    template = 'orderable/edit_inline/tabular.html'
