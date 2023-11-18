from django.contrib.admin import *
from .models import UserDop

@register(UserDop)
class CustomUserAdmin(ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')


