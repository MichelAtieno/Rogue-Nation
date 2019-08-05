from django.urls import path
from .views import home, news

app_name= 'core'

urlpatterns = [
    path('', home, name="item-list"),
    path('news', news, name="news"),
]