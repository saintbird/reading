from django.contrib import admin
from .models import BookInfo

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','rates','votes','tag')    
    list_filter = ('tag','rates') 

admin.site.register(BookInfo,BookAdmin)