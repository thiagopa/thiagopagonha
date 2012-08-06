from django import template

from random import sample

register = template.Library()



from blog.models import *

@register.inclusion_tag('blog/categories.html')
def blog_categories():
    return {
            'categories': Category.objects.all(),
    }
    
@register.inclusion_tag('blog/archive.html')
def blog_archive():
    return {
            'archives': Post.objects.dates('published', 'month', order='DESC'),
    }
    
@register.inclusion_tag('blog/profiles.html')
def profile_links():
    return {
            'links' : Links.objects.filter(type=1)
    }    

@register.inclusion_tag('blog/profiles.html')
def afiliates_links():
    return {
            'links' : Links.objects.filter(type=2)
    }    
    
@register.inclusion_tag('blog/fortuneCookies.html')
def fortune_cookies():
    return { 
            'fortune_cookies' : sample(FortuneCookie.objects.all(),3) 
    }