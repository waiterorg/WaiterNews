from django import template
from ..models import Category, Article
from main_account.models import LogoLogin

register = template.Library()

@register.inclusion_tag("shared/navigation.html")
def category_navbar(request):
    return {
        "categories": Category.objects.get_active_category(),
        "request": request,
    }

@register.inclusion_tag("registration/logo.html")
def logo_picture():
    return {
        "logo": LogoLogin.objects.get_active_logo(),
    }

@register.inclusion_tag("shared/popular_articles.html")
def popular_articles():
    return {
        "popular_articles": Article.objects.get_popular_articles(),
    }

@register.inclusion_tag("shared/top_rated_articles.html")
def top_rated_articles():
    return {
        "top_rated_articles": Article.objects.get_top_rated_articles(),
    }

@register.inclusion_tag("shared/hot_article.html")
def hot_articles():
    return {
        "hot_articles": Article.objects.get_hot_articles(),
    }



@register.inclusion_tag("registration/partials/link.html")
def link(request, link_name, content, classes):
    return {
        "request": request,
        "link_name": link_name,
        "link": "account:{}".format(link_name),
        "content": content,
        "classes": classes,
    }
