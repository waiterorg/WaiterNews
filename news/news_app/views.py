from django.shortcuts import get_object_or_404, render
from .models import Article
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.get_published_article()
    paginate_by = 4

class ArticleDetail(DetailView):

    def get_object(self):
        slug = self.kwargs.get('slug')
        article = Article.objects.get_published_article()
        article = get_object_or_404(article, slug=slug)

        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)

        return article
