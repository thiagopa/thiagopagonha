from django.conf.urls.defaults import *
from psn.views import * 

urlpatterns = patterns('wiki.views',
   (r"^$", "index"),
   (r"^([a-zA-Z0-9-]+)/$", "get_page_name")
)
