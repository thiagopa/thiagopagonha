#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from suds.client import Client

from psn.settings import *

from psn.mem_cache import MemCache

from suds.cache import NoCache

def profile(request):
    
    # Necessário esse cache porque o AppEngine não permite escritas em arquivos
    client = Client(PSN_WSDL, cache=MemCache())
    
    profile = client.service.GetProfile(PSN_USER)
    
    return render_to_response('psn.html', dict(profile=profile))
    
