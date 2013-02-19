from django.conf.urls.defaults import *
from django.views.generic import list_detail, date_based
from blog.models import *
from blog.views import * 
from blog.feeds import BlogLatestEntries

feeds = {
    'latest': BlogLatestEntries,
}

urlpatterns = patterns('blog.views',
   (r"^(?P<slug>[a-z-]+)/$", "post"),
   (r"^month/(\d+)/(\d+)/$", "month"),
   (r"^notify$", "send_mail"),
   
   #url(r'^post/(?P<slug>[a-z-]+)/$', blog_generic_view, 
    #    {'redirect_to': list_detail.object_detail, 'slug_field': 'slug', 'paginated': False,}, name="single_post"),
    #url(r'^$', blog_generic_view, 
    #    {'redirect_to': list_detail.object_list}, name="blog_home"),
    #url(r'^archive/(?P<month>[a-z]+)/(?P<year>\d{4})/$', blog_generic_view,
    #    {'redirect_to': date_based.archive_month, 'date_field': 'published', 'template_name': 'blog/post_list.html',}
    #        , name="blog_posts_by_month"),
    #url(r'^category/(\d+)/$', blog_posts_by_category, name="blog_posts_by_category"),
    #url(r'^search/$', blog_post_search, name="blog_post_search"),
    
    #(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.Feed', {'feed_dict': feeds}),
   
   
#   (r'^comments/', include('django.contrib.comments.urls')),
   url(r'^(?P<template>\w+)/$', static_page, name="static_page"),
#   url(r'^post/(?P<object_id>\d+)/$', list_detail.object_detail, {'queryset': Post.objects.all(), 'template_object_name': 'post',}, name="single_post"),
   (r"", "main"),
   #url(r'^$', list_detail.object_list, {'queryset': Post.objects.all(), 'template_object_name': 'post',}, name="blog_home"),
   #(r'^$', "about"),
   #url(r"^$", static_page, { 'template' : 'list' }, name="static_page"),
)
