from django.urls import path
from .views import home, news, post

app_name= 'core'

urlpatterns = [
    path('', home, name="item-list"),
    path('news', news, name="news"),
    path('post/<id>/', post, name="post"),
]