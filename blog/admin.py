from django.contrib import admin

from blog.models import Category, Article, Commentary


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ['id', 'title', "author", 'author__username']


@admin.register(Commentary)
class AdminCommentary(admin.ModelAdmin):
    list_display = ['id', "author", 'author__username', 'article', 'article__title']



