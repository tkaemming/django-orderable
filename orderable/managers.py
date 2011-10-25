from django.db import models
from orderable import settings

# TODO: eventually allow with_respect_to field to be a lookup

class OrderableManager(models.Manager):
    use_for_related_fields = True

    def __init__(self, ordering_field=None, with_respect_to=None, *args, **kwargs):
        super(OrderableManager, self).__init__(*args, **kwargs)

        self._with_respect_to = with_respect_to

        if ordering_field is None:
            ordering_field = settings.DEFAULT_ORDERING_FIELD
        self._ordering_field = ordering_field

    def get_next(self, obj):
        if self._with_respect_to:
            queryset = self.in_order_limited_to_siblings(obj)
        else:
            queryset = self.in_order()
        return queryset.filter(order__gt=getattr(obj, self._ordering_field))[0:1].get()

    def get_previous(self, obj):
        if self._with_respect_to:
            queryset = self.in_order_limited_to_siblings(obj)
        else:
            queryset = self.in_order()
        return queryset.filter(order__lt=getattr(obj, self._ordering_field))[0:1].get()

    def in_order(self, reverse=False):
        fields = [self._ordering_field, 'pk']
        if self._with_respect_to:
            fields.insert(0, self._with_respect_to)

        if reverse:
            fields = ['-%s' % field for field in fields]

        return self.order_by(*fields)

    def in_order_limited_to_siblings(self, obj, *args, **kwargs):
        queryset = self.in_order(*args, **kwargs)
        return queryset.filter(**{
            self._with_respect_to: getattr(obj, self._with_respect_to)
        })
