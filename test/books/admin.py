from django.contrib import admin
from orderable.admin import OrderableModelAdmin
from books.models import Book, Chapter

class ChapterInline(admin.TabularInline):
    model = Chapter

class BookAdmin(OrderableModelAdmin):
    inlines = (ChapterInline,)

admin.site.register(Book, BookAdmin)
