#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from suds.client import Client

from psn.settings import *

from suds.mem_cache import MemCache

def profile(request):
    
    try :
        psn_user = request.POST[SEARCH_PARAM]
    except :
        psn_user = PSN_USER
    
    # Necessário esse cache porque o AppEngine não permite escritas em arquivos
    client = Client(PSN_WSDL, cache=MemCache())
    
    try : 
        profile = client.service.GetProfile(psn_user)
    except :
        profile = None
    
    return render_to_response('psn.html', dict(profile=profile,psn_user=psn_user))
    
