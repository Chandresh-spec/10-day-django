from django.contrib import admin
from .models import Blogs
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    field=('text','blog_type','created_at')
    ordering=('created_at',)
    list_filter=('blog_type',)
    search_fields=('blog_name',)




admin.site.register(Blogs,BlogAdmin)

