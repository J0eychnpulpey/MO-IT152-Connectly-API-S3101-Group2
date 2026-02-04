from django.contrib import admin
from .models import User, Post, Comment

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_verified', 'created_at']
    list_filter = ['is_verified', 'created_at']
    search_fields = ['username', 'email']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'author', 'is_published', 'created_at']
    list_filter = ['is_published', 'created_at']
    search_fields = ['content']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'author', 'post', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text']