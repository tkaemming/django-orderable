from django.core.exceptions import ObjectDoesNotExist

def increment_order_field(sender, instance, **kwargs):
    # TODO: Don't assume that this is the default manager.
    manager = sender._default_manager
    ordering_field = manager._ordering_field

    # TODO: Maybe only do iths if this is a new object?
    if getattr(instance, ordering_field) is None:
        try:
            last = manager.in_order(reverse=True)[0:1].get()
            order = getattr(last, ordering_field, None)
            if order is not None:
                instance.order = order + 1
        except ObjectDoesNotExist:
            pass

    # If we weren't able to set the order above, assume it's the first object in order.
    # TODO: Is this a safe assumption?
    if instance.order is None:
        instance.order = 1
