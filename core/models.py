from django.conf import settings
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class NewsItem(models.Model):
    title = models.CharField(max_length=100)
    news_story = models.CharField(max_length=1000, default="")
    image = models.ImageField(upload_to="news_media/", blank=True)
    date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title



class Client(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

class SignUp(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.email