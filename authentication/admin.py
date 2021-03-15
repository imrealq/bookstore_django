from django.contrib import admin

# Register your models here.

from .models import BooksInfo, Author

admin.site.register(BooksInfo)
admin.site.register(Author)