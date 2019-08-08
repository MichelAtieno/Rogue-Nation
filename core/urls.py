from django.urls import path
from .views import home, news, post, search, news_letter, get_artist, artist_profile

app_name= 'core'

urlpatterns = [
    path('', home, name="item-list"),
    path('news', news, name="news"),
    path('post/<id>/', post, name="post"),
    path('search/',search, name="search"),
    path('newsletter/',news_letter, name="newsletter"),
    path('artists/',get_artist, name="artist"),
    path('artist/<id>',artist_profile, name="artist_profile"),
]