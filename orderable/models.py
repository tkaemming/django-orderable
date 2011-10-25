from django.core.exceptions import ObjectDoesNotExist
from django.db import models

class OrderableModel(models.Model):
    """
    Provides basic facilities for ordered model instances.
    """
    order = models.PositiveIntegerField(db_index=True, blank=True, null=True)
    
    def _get_ordering_queryset(self):
        """
        Returns the queryset used for model ordering. 
        
        This can helpful (or even required) in some special cases, such as
        using model inheritance or polymorphic model implementations where the
        models returned by the default manager are not necessarily those that
        should be ordered on.
        """
        return self.__class__._default_manager.all()
    
    def save(self, *args, **kwargs):
        """
        Save the current model instance, and set the model order if none has
        been previously set.
        """
        queryset = self._get_ordering_queryset()
        
        if self.order is None:
            try:
                last_object = queryset.order_by('-order', '-id')[0:1].get()
                if last_object.order is not None:
                    self.order = last_object.order + 1
            except ObjectDoesNotExist:
                pass
        
        # If we weren't able to set the order above, assume it's the first
        # object in order.
        if self.order is None:
            self.order = 1
        
        super(OrderableModel, self).save(*args, **kwargs)
    
    def get_previous(self, queryset=None):
        """
        Return the previous model in order (if available).
        
        Throws (or technically, allows to bubble up) the appropriate 
        ObjectDoesNotExist exception if the object does not exist.
        """
        if queryset is None:
            queryset = self._get_ordering_queryset()
            
        return queryset.order_by('-order', '-id').filter(order__lt=self.order)[0:1].get()

    def get_next(self, queryset=None):
        """
        Return the next model in order (if available).
        
        Throws (or technically, allows to bubble up) the appropriate 
        ObjectDoesNotExist exception if the object does not exist.
        """
        if queryset is None:
            queryset = self._get_ordering_queryset()
        
        return queryset.order_by('order', 'id').filter(order__gt=self.order)[0:1].get()
    
    class Meta:
        abstract = True
        ordering = ('order',)