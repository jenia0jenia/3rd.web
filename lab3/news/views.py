from django.shortcuts import render
from news.models import News


def index(request):
    context = {'news_list': News.objects.all()}
    return render(request, 'index.html', context)

# Create your views here.
