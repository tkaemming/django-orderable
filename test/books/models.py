from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from orderable.managers import OrderableManager
from orderable.models import OrderableModelMixin
from orderable.listeners import increment_order_field

class Book(OrderableModelMixin, models.Model):
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField()

    objects = OrderableManager()

    def __unicode__(self):
        return u'%s' % self.title

pre_save.connect(increment_order_field, sender=Book)

class Chapter(OrderableModelMixin, models.Model):
    book = models.ForeignKey(Book)
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField()

    objects = OrderableManager(with_respect_to='book')

    def __unicode__(self):
        return u'%s' % self.title
