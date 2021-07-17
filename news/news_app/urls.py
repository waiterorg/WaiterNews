from django.urls import path
from .views import ArticleListView

app_name = 'news'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articlelist'),
]