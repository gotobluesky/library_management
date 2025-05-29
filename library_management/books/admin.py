from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'ISBN', 'page_count', 'availability')  # use 'availability'
    search_fields = ('title', 'author', 'ISBN')
    list_filter = ('availability',)  # use 'availability' here as well
  
admin.site.register(Book, BookAdmin)