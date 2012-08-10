from django.conf.urls.defaults import *
from psn.views import * 

urlpatterns = patterns('psn.views',
   (r"^$", "profile"),
)
