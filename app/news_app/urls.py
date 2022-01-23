from django.urls import path
from .views import ArticleListView, ArticleDetail, CategoryList, AuthorList, mail_weekely_articles

app_name = 'news'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articlelist'),
    path('page/<int:page>', ArticleListView.as_view(), name='articlelist'),
    path('news/<slug:slug>', ArticleDetail.as_view(), name='articledetail'),
    path('category/<slug:slug>', CategoryList.as_view(), name='CategoryView'),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name='CategoryView'),
    path('author/<slug:username>', AuthorList.as_view(), name='AuthorView'),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name='AuthorView'),
    path('send-email/weekely-articles', mail_weekely_articles, name='mail-weekely-articles'),
]