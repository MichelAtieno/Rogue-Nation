from django.shortcuts import render
from .models import NewsItem

# Create your views here.

def home(request):
    context = {
        'news': NewsItem.objects.all()
    }
    return render(request, "news.html", context)
