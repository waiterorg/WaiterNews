from django import template
from ..models import Category, Article


register = template.Library()

@register.inclusion_tag("shared/navigation.html")
def category_navbar():
    return {
        "categories": Category.objects.get_active_category(),
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
