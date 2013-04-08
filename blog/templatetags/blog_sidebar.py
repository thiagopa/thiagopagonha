from django import template

from random import sample

register = template.Library()

from blog.models import *

@register.inclusion_tag('blog/profiles.html')
def profile_links():
    return {
            'links' : Links.objects.filter(type=1)
    }    

@register.inclusion_tag('blog/profiles.html')
def afiliates_links():
    
    try:
        links = Links.objects.filter(type=2)
        links = sample(links,3)
    except ( ValueError ):    
        links = None
        
    return {
            'links' : links
    }    
    
@register.inclusion_tag('blog/fortuneCookies.html')
def fortune_cookies():
    try:
        fortune = FortuneCookie.objects.all()
        fortune = sample(fortune,3)
    except ( ValueError ):    
        fortune = None

    return { 
            'fortune_cookies' : fortune 
    }