#-*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from blog.models import Post
from django.core.urlresolvers import reverse

class BlogLatestEntries(Feed):
    title = "Thiago Pagonha"
    link = "/blog/"
    description = "Últimas notícias no blog."
    
    def items(self):
        return Post.objects.filter(visible=True)[:5]
    
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.short_description

    def item_link(self, item):
        return reverse('blog.views.post', args=[item.slug])