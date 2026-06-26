from django.contrib import admin
from .models import Category, Tag, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
        'category',
        'created_at'
    )

    search_fields = (
        'title',
        'content'
    )

    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'post',
        'is_approved',
        'created_at'
    )

    list_filter = (
        'is_approved',
        'created_at'
    )