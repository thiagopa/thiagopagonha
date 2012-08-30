#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from wiki.models import Page

def index(self):
    
    return get_page_name(self,'index')
    

def get_page_name(self, pagename):
    try :
        page = Page.objects.get(name=pagename)
    except (ObjectDoesNotExist) :        
        raise Http404 
        
    return render_to_response('wiki.html',dict(wiki=page))

