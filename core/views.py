from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import NewsItem, SignUp

# Create your views here.

def search(request):
    queryset = NewsItem.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)|
            Q(news_story__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }

    return render(request, 'search_results.html', context)

def get_category_count():
    queryset = NewsItem.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset

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
    category_count = get_category_count()
    # print(category_count)
    most_recent = NewsItem.objects.order_by('-date')[0:6]
    news = NewsItem.objects.all()
    paginator = Paginator(news, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
        'category_count': category_count
    }
    return render(request, "news.html", context)

def post(request, id):
    
    return render(request, 'post.html')