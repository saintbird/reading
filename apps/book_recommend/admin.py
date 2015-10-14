from django.contrib import admin
from .models import BookInfo
from .models import MainTag
from .models import SubTag

# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ('title','author','rates','votes')    
    list_filter = ('tag','rates')
    search_fields=['title', 'author']
    
class MainTagAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    
class SubTagAdmin(admin.ModelAdmin):
    list_display = ('name','parent')
    list_filter = ('parent',)

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(MainTag,MainTagAdmin)
admin.site.register(SubTag,SubTagAdmin)