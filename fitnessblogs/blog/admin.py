from django.contrib import admin
from blog.models import blogpost, Post, BlogComment
# Register your models here.


admin.site.register(blogpost)
admin.site.register((BlogComment))


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinymce.js',)
    

