from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class NewsItem(models.Model):
    title = models.CharField(max_length=100)
    news_story = models.CharField(max_length=1000, default="")
    image = models.ImageField(upload_to="news_media/", blank=True)
    date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:post',kwargs={
            'id': self.id
        })



class Artist(models.Model):
    image = models.ImageField(upload_to="artist_media/", blank=True)
    name = models.CharField(max_length=100, default="artist")
    start_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name

class SignUp(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.email