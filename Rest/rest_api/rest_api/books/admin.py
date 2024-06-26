from django.contrib import admin
from rest_api.books.models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author')