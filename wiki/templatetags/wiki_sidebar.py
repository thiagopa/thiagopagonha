from django import template

register = template.Library()

from wiki.models import *

@register.inclusion_tag('wiki_side.html')
def last_pages():
    return {
            'last_pages': Page.objects.order_by("-updated")[:5]
    }
    
