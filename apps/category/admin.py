from django.contrib.admin import *
from .models import Category

@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

    