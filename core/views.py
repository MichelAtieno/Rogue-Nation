from django.shortcuts import render
from .models import NewsItem, SignUp

# Create your views here.

def home(request):
    queryset = NewsItem.objects.filter(featured=True)
    latest = NewsItem.objects.order_by('-date')[0:3]
    
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = SignUp()
        new_signup.email = email
        new_signup.save()
    
    context = {
      'object_list': queryset,
      'latest': latest
    }
    return render(request, "home_page.html", context)

def news(request):
    context = {
        'news': NewsItem.objects.all()
    }
    return render(request, "news.html", context)
