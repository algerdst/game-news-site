from django.contrib import admin

from .models import Article, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'date', 'popular', 'slug']
    list_editable = ['category', 'popular', 'slug']
    prepopulated_fields = {'slug': ('name',)}
