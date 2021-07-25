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

@register.inclusion_tag("registration/partials/link.html")
def link(request, link_name, content, classes):
    return {
        "request": request,
        "link_name": link_name,
        "link": "account:{}".format(link_name),
        "content": content,
        "classes": classes,
    }
