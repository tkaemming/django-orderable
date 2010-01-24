from django.core.exceptions import ObjectDoesNotExist
from django.db import models

class OrderableModel(models.Model):
    """
    Provides basic facilities for ordered model instances.
    """
    order = models.PositiveIntegerField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        """
        Save the current model instance, and set the model order if none has
        been previously set.
        """
        manager = self.__class__._default_manager
        
        if self.order is None:
            try:
                last_object = manager.order_by('-order', '-id')[0:1].get()
                if last_object.order is not None:
                    self.order = last_object.order + 1
            except ObjectDoesNotExist:
                pass
        
        # If we weren't able to set the order above, assume it's the first
        # object in order.
        if self.order is None:
            self.order = 1
        
        super(OrderableModel, self).save(*args, **kwargs)
    
    def get_previous(self):
        """
        Return the previous model in order (if available).
        
        Throws (or technically, allows to bubble up) the appropriate 
        ObjectDoesNotExist exception if the object does not exist.
        """
        manager = self.__class__._default_manager
        return manager.order_by('-order', '-id').filter(order__lt=self.order)[0:1].get()

    def get_next(self):
        """
        Return the next model in order (if available).
        
        Throws (or technically, allows to bubble up) the appropriate 
        ObjectDoesNotExist exception if the object does not exist.
        """
        manager = self.__class__._default_manager
        return manager.order_by('order', 'id').filter(order__gt=self.order)[0:1].get()
    
    class Meta:
        abstract = True
        ordering = ('order',)