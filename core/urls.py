from django.urls import path
from .views import home, news, post, search

app_name= 'core'

urlpatterns = [
    path('', home, name="item-list"),
    path('news', news, name="news"),
    path('post/<id>/', post, name="post"),
    path('search/',search, name="search"),
]