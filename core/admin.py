from django.contrib import admin
from .models import NewsItem, Client, Category, SignUp

# Register your models here.

admin.site.register(NewsItem)
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(SignUp)