from django.contrib import admin

from .models import Blog, Blogger, Comment, LogRequest


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'post_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'blog', 'content', 'post_date']


@admin.register(LogRequest)
class LoginRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'path', 'method', 'timestamp']
