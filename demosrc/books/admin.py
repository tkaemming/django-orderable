from django.contrib import admin
from orderable.admin import (OrderableAdmin, OrderableStackedInline,
    OrderableTabularInline)
from books.models import Book, Chapter, Review

class ChapterInlineAdmin(OrderableTabularInline):
    model = Chapter
    extra = 0
    fieldsets = (
        (None, {'fields': ('title', 'order'),}),
    )

class ReviewInlineAdmin(OrderableStackedInline):
    model = Review
    extra = 0
    fieldsets = (
        (None, {'fields': ('review', 'rating', 'order'),}),
    )


class BookAdmin(OrderableAdmin):
    list_display = ('title', 'author', 'pages')
    model = Book
    inlines = [ChapterInlineAdmin, ReviewInlineAdmin]

admin.site.register(Book, BookAdmin)
