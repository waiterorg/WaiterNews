from django.shortcuts import get_object_or_404, render
from .models import Article, Category
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

class CategoryList(ListView):
    paginate_by = 4
    template_name = 'news_app/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(
            Category.objects.get_active_category(), slug=slug)
        return category.articles.get_published_article()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context

def login(request):
    return render(request,'registration/login.html',{})