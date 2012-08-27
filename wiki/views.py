#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from wiki.models import Page

def index(request):
    
    return render_to_response('wiki.html')
    

def get_page_name(self, pagename):
    page = Page.objects.get(name=pagename)
    
    if page == None :
        raise "Page Not Found"
        
    return render_to_response('wiki.html',dict(wiki=page))

