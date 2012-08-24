from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/blog/about/', }),
    (r'^blog/', include('blog.urls')),
    (r'^psn/', include('psn.urls')),
    (r'^wiki/', include('wiki.urls')),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    #('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^google9bee04d2de3a930d.html$', 'blog.views.google') 
)
