from django.conf.urls.defaults import *
from django.views.generic import list_detail, date_based
from blog.models import *
from blog.views import * 

urlpatterns = patterns('blog.views',
   (r"^preview/(\d+)$", "preview"),
   (r"^publish/(\d+)$", "publish"),
   (r"^(?P<slug>[a-zA-Z0-9-]+)/$", "post"),
   (r"^notify$", "send_mail"),
   (r"^archive$", "archive"),
   (r"^category/(\d+)/$", "category"),
    #url(r'^category/(\d+)/$', blog_posts_by_category, name="blog_posts_by_category"),
    #url(r'^search/$', blog_post_search, name="blog_post_search"),
   
   url(r'^(?P<template>\w+)/$', static_page, name="static_page"),
   (r"", "main"),
)
