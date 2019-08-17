from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import NewsItem, SignUp, Artist, Athlete,Category

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

def get_category():
    queryset = Athlete.objects.values('categories__title')
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
    news = get_object_or_404(NewsItem, id=id)
    context = {
        'news': news
    }
    return render(request, 'post.html', context)

def news_letter(request):

    return render(request, 'news_letter.html')

def get_artist(request):
    artists = Artist.objects.all()


    context = {
     'artists': artists
    }
    return render(request, 'artists.html', context)

def artist_profile(request, id):
    artist = get_object_or_404(Artist, id=id)
    queryset = NewsItem.objects.all()
    query = artist.name
    queryset = queryset.filter(
        Q(title__icontains=query)|
        Q(news_story__icontains=query)
    ).distinct()
    context = {
        'artist': artist,
        'queryset': queryset
    }
    return render(request, 'artist_profile.html', context)

def get_athlete(request):
    category = get_category()
    athletes = Athlete.objects.all()
    all_categories = Category.objects.all()

    context = {
     'athletes':athletes,
     'category': category,
     'all_categories': all_categories
    }
    return render(request, 'athletes.html', context)

def athlete_profile(request, id):
    athlete = get_object_or_404(Athlete, id=id)
    queryset = NewsItem.objects.all()
    query = athlete.name
    queryset = queryset.filter(
        Q(title__icontains=query)|
        Q(news_story__icontains=query)
    ).distinct()
    context = {
        'athlete': athlete,
        'queryset': queryset
    }
    return render(request, 'athlete_profile.html', context)

def category_profile(request, id):
    one_category = get_object_or_404(Category, id=id)
    cat_queryset = Athlete.objects.all()
    cat_query = one_category.title
    cat_queryset = cat_queryset.filter(Q(categories__title__icontains=cat_query)).distinct()
    context = {
        'one_category': one_category,
        'queryset': cat_queryset
     }
    return render(request, 'category.html', context)


