from django.contrib import admin

# Register your models here.

from .models import Author, Category, Post, PostCategory, Comment
 
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)

