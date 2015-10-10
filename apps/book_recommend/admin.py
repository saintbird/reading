from django.contrib import admin
from .models import BookInfo

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','rates','votes')    
    list_filter = ('tag','rates')
    search_fields=['title', 'author']

admin.site.register(BookInfo,BookAdmin)