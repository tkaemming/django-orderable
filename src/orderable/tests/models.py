from django.db import models
from orderable.models import OrderableModel

class Book(OrderableModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pages = models.PositiveIntegerField()
    
    def __unicode__(self):
        return u'%s' % self.title