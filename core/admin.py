from django.contrib import admin
from .models import NewsItem, Client

# Register your models here.

admin.site.register(NewsItem)
admin.site.register(Client)