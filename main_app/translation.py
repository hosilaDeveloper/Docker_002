from modeltranslation.translator import register, TranslationOptions, translator
from .models import Post


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'author',)


translator.register(Post, PostTranslationOptions)
