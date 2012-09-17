from django import template

from random import sample

import xml.parsers.expat

import logging

logger = logging.getLogger(__name__)

register = template.Library()

from psn.models import *

@register.inclusion_tag('psn_side.html')
def wish_list():
    return {
            'wishlist': WishList.objects.all(),
    }
    
@register.inclusion_tag('psn_px.html')
def progress_ratio(value,ratio):
    
    result = float(value) * float(ratio)
    
    if result < 1 : 
        result = 1
    
    return {
        'result' : "%f" % result
    }
