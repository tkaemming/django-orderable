from django.db import models
from orderable import settings

class OrderableManager(models.Manager):
    use_for_related_fields = True

    def __init__(self, ordering_field=None, auto_increment_ordering_field=True, 
            with_respect_to=None, *args, **kwargs):
        super(OrderableManager, self).__init__(*args, **kwargs)

        self._with_respect_to = with_respect_to

        if ordering_field is None:
            ordering_field = settings.DEFAULT_ORDERING_FIELD
        self._ordering_field = ordering_field

        if auto_increment_ordering_field:
            pass # TODO: Attach signal to the model.

    def get_next(self, obj):
        queryset = self
        # TODO: Add `with_respect_to` support.
        return queryset.order_by('%s' % self._ordering_field, 'pk').filter(
            order__gt=getattr(obj, self._ordering_field))[0:1].get()

    def get_previous(self, obj):
        queryset = self
        # TODO: Add `with_respect_to` support.
        return queryset.order_by('-%s' % self._ordering_field, '-pk').filter(
            order__lt=getattr(obj, self._ordering_field))[0:1].get()
