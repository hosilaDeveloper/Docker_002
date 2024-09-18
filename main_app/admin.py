from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Post


# Register your models here.

class PostAdmin(TranslationAdmin):
    list_display = ('title', 'content', 'author',)


admin.site.register(Post, PostAdmin)
