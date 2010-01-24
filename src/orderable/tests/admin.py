from django.contrib import admin
from orderable.admin import OrderableAdmin, OrderableStackedInline, \
    OrderableTabularInline
from orderable.tests.models import Book, Chapter, Review

class ChapterAdmin(OrderableTabularInline):
    model = Chapter

class ReviewAdmin(OrderableStackedInline):
    model = Review

class BookAdmin(OrderableAdmin):
    list_display = ('title', 'author', 'pages')
    model = Book
    inlines = [ChapterAdmin, ReviewAdmin]

admin.site.register(Book, BookAdmin)