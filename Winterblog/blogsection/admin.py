from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')  # Display these fields in the list view
    search_fields = ('title', 'author')  # Add search capability by title and author
    list_filter = ('created_at', 'author')  # Add filters for creation date and author
    ordering = ('-created_at',)  # Default ordering by creation date (newest first)