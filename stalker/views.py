#-*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response

from stalker.models import *

def get_profiles(request):
    d = {}
    return render_to_response("profiles.html", d)
