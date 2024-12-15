from django.contrib import admin
from .models import Post, Item, List
from django_summernote.admin import SummernoteModelAdmin
#from .models import SomeModel

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')  # Display these fields in the list view
    search_fields = ('title', 'author')  # Add search capability by title and author
    list_filter = ('created_at', 'author')  # Add filters for creation date and author
    ordering = ('-created_at',)  # Default ordering by creation date (newest first)


class ItemAdmin(SummernoteModelAdmin):
    list_display = ('item_name', 'item_desc', 'item_price')

# Apply summernote to all TextField in model.
#class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
#    summernote_fields = '__all__'

#admin.site.register(SomeModel, SomeModelAdmin)

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Item, PostAdmin)
admin.site.register(List)