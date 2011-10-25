class OrderableModelMixin(object):
    def get_next(self):
        # TODO: Don't assume the default manager is orderable.
        return self._default_manager.get_next(self)

    def get_previous(self):
        # TODO: Don't assume the default manager is orderable.
        return self._default_manager.get_previous(self)
