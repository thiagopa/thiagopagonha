#-*- coding: utf-8 -*-
import time

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

from blog.models import *
from django.forms import ModelForm

from django.views.generic import list_detail

from google.appengine.api import mail

import json

MONTH_NAME = ['[X]', 'Janeiro', 'Fevereiro' , 'Março' , 'Abril' , 'Maio' , 'Junho' , 'Julho' , 'Agosto' , 'Setembro' , 'Outubro', 'Novembro' , 'Dezembro']

def static_page(response, template):
    template = "%s.html" % (template)
    return render_to_response(template)

def post(request, slug):
    try :
        post = Post.objects.filter(slug=slug,visible=True)[0]
    
        post.views_count += 1;
    
        post.save()
    
        d = dict(post=post)
        d.update(csrf(request))
        return render_to_response("post.html", d)
    except Exception:
        return HttpResponseNotFound(render_to_string('404.html'))

def preview(request, id):
    """Single post with comments and a comment form."""
    try :
        post = Post.objects.get(id=id)
    
        d = dict(post=post)
        d.update(csrf(request))
        return render_to_response("preview.html", d)
    except Exception:
        return HttpResponseNotFound(render_to_string('404.html'))

def publish(request, id):
    """Single post with comments and a comment form."""
    try :
        post = Post.objects.get(id=id)
    
        post.visible = True
        
        post.save()
    
        d = dict(post=post)
        d.update(csrf(request))
        return render_to_response("post.html", d)
    except Exception:
        return HttpResponseNotFound(render_to_string('404.html'))

def archive(request):
    if not Post.objects.count(): return []
    
    content = []
    try :
        id = request.GET['node']
    except Exception :
        id = None
    
    if not id :
        year, month = time.localtime()[:2]
        first = Post.objects.order_by("created")[0]
        fyear = first.created.year
        fmonth = first.created.month
        
        for y in range(year, fyear-1, -1):
            
            year_map = {
                 "label": y,
                 "id": y,
                 "load_on_demand": True
            }
            
            content.append(year_map)
    elif len(id) == 4 :
        months = []
        posts = Post.objects.filter(created__year=id,visible=True)
        for p in posts:
            month = p.created.month
            if not month in months:
                months.append(month)
                month_map = {
                "label" : MONTH_NAME[month],
                "id" : str(id) +'.'+ str(month),
                "load_on_demand": True
                }
                content.append(month_map)
    else :
        splited = id.split('.') 
        year = splited[0]
        month = splited[1]
        
        posts = Post.objects.filter(created__year=year,visible=True)

        for p in posts:
            m = p.created.month
            if m == int(month):
                post_map = {
                    "label" : '<a href="/blog/%s/">%s</a>' % (p.slug,p.title)
                }
                content.append(post_map)
        
    return HttpResponse(json.dumps(content), content_type="application/json")


def main(request):
    posts = Post.objects.filter(visible=True)
    return paginator(request,posts)

def paginator(request, posts):
    """Main listing."""
    paginator = Paginator(posts, 3)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("list.html", dict(posts=posts, post_list=posts.object_list))

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(categories=category, visible=True)
    
    return paginator(request,posts)

def blog_post_search(request):
    if 's' in request.GET and request.GET['s']:
        s = request.GET['s']
        return blog_generic_view(
            request,
            list_detail.object_list,
        )
    else:
        return render_to_response('blog/invalid_search.html')
        
def google(request):
    return render_to_response('google9bee04d2de3a930d.html')

def send_mail(request):
    """
       Adiciona o contador 
    """
    
    url = request.GET['message']    
    
    post = Post.objects.get(slug=url.rsplit('/',2)[1])
    
    post.comment_count += 1;
    
    post.save()
    
    """
        Envia Email para Notificar o Novo Comentário
    """
    mail.send_mail(sender="Thiago Pagonha <thi.pag@gmail.com>",
                   to="Thiago Pagonha <thi.pag@gmail.com>",
                   subject="thiagopagonha.appspot.com: New Comment Has Arrived!",
                   body="""
                            Comment was added at '%s': \n\n
                        """ % (url))
      
    return HttpResponse(status=200)
