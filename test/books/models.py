from django.db import models
from orderable.managers import OrderableManager

class Book(models.Model):
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField()

    objects = OrderableManager()

    def __unicode__(self):
        return u'%s' % self.title

class Chapter(models.Model):
    book = models.ForeignKey(Book)
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField()

    objects = OrderableManager(with_respect_to='book')

    def __unicode__(self):
        return u'%s' % self.title
