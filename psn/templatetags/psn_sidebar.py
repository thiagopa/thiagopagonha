from django import template

from random import sample

register = template.Library()

from psn.models import *

@register.inclusion_tag('psn_side.html')
def wish_list():
    return {
            'wishlist': WishList.objects.all(),
    }
    
