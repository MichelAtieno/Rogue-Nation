from django.conf import settings
from django.db import models

# Create your models here.
class NewsItem(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Client(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   
    start_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username