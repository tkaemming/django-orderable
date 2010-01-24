from django.contrib import admin
from orderable.admin import OrderableAdmin
from orderable.tests.models import Book

class BookAdmin(OrderableAdmin):
    list_display = ('title', 'author', 'pages')
    model = Book

admin.site.register(Book, BookAdmin)