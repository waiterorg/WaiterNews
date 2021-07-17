from django.urls import path
from .views import ArticleListView, ArticleDetail

app_name = 'news'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articlelist'),
    path('news/<slug:slug>', ArticleDetail.as_view(), name='articledetail'),

]