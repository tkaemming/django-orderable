from django.db import models
from orderable.models import BaseOrderableModel, OrderableModel
from django.template.defaultfilters import truncatewords


class Book(OrderableModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pages = models.PositiveIntegerField()

    def __unicode__(self):
        return u'%s' % self.title

class Chapter(OrderableModel):
    book = models.ForeignKey(Book)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.title

class Review(BaseOrderableModel):
    book = models.ForeignKey(Book)
    review = models.TextField()
    rating = models.PositiveIntegerField()

    # Test that we can manually define `order` field when using
    # BaseOrderableModel. Note we need `blank=True` and we should also
    # set `ordering = ('order',)` in class Meta.
    order = models.PositiveIntegerField(db_column='item_order', db_index=True,
        blank=True)

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return u"%s" % truncatewords(self.review, 10)
