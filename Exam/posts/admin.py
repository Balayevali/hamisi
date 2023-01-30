from django.contrib import admin

from .models import Author, Category, Post, Comment,Exam

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Exam)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')