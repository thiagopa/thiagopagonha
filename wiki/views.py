#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

def index(request):
    
    return render_to_response('wiki.html')
    
