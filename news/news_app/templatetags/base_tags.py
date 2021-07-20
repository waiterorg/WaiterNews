from django import template
from ..models import Category, Article


register = template.Library()

@register.inclusion_tag("shared/navigation.html")
def category_navbar():
    return {
        "categories": Category.objects.get_active_category(),
    }