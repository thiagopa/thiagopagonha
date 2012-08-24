from django.conf.urls.defaults import *
from psn.views import * 

urlpatterns = patterns('wiki.views',
   (r"^$", "index"),
)
