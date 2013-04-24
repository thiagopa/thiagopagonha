#-*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.inclusion_tag('blog/comment_decorator.html')
def comment_decorator(comments):
    
    if comments==0 :
        message = "Nenhum Comentário"
    elif comments==1:
        message = "Apenas UM Comentário"
    else :
        message = "%d Comentários" % (comments)
    
    return {
            'message' : message
    }    

