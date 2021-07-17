from django.shortcuts import render
from .models import Article
from django.views.generic.list import ListView
# Create your views here.

class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.get_published_article()
    paginate_by = 4