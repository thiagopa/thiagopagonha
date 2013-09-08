from django.conf.urls.defaults import *
from django.views.generic import list_detail, date_based
from stalker.models import *
from stalker.views import * 

urlpatterns = patterns('stalker.views',
   (r"", "get_profiles"),
)
