from django.contrib import admin
from .models import NewsItem, Artist, Category, SignUp, Athlete

# Register your models here.

admin.site.register(NewsItem)
admin.site.register(Artist)
admin.site.register(Category)
admin.site.register(SignUp)
admin.site.register(Athlete)