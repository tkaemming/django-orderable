from django.db import models

class Orderable(models.Model):
    order = models.PositiveIntegerField(blank=True, null=True)
    
    class Meta:
        abstract = True
        ordering = ('order',)