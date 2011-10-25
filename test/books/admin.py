from django.contrib import admin
from orderable.admin import OrderableModelAdmin, OrderableTabularInline
from books.models import Book, Chapter

class ChapterInline(OrderableTabularInline):
    model = Chapter

class BookAdmin(OrderableModelAdmin):
    inlines = (ChapterInline,)

admin.site.register(Book, BookAdmin)
