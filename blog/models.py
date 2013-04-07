from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.safestring import mark_safe
from wiki.models import default_now

class Category(models.Model):
    name = models.CharField(max_length=60)
    
    def __unicode__(self):
        return self.name

class PostManager(models.Manager):
    def search(self, search_string):
        search_string = search_string.strip()
        
        queryset = self.get_query_set()
        return queryset.filter(models.Q(title__icontains=search_string) | models.Q(body__icontains=search_string))


class Post(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=120, unique=True)
    body = models.TextField()
    created = models.DateTimeField(default=default_now)
    categories = models.ForeignKey(Category)
    
    short_description = models.CharField(max_length=60)

    views_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    
    visible = models.BooleanField(default=True)
    
    objects = PostManager()
    
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Links(models.Model):
    
    TYPES = (
         (1, 'PROFILE'), 
         (2, 'AFFILIATES')
    )
    
    name = models.CharField(max_length=60)
    url = models.TextField()
    type = models.IntegerField(choices=TYPES)
    
class FortuneCookie(models.Model):
    name = models.TextField()
        
### Admin

class PostAdmin(admin.ModelAdmin):
    def preview_post(self,obj):
        return mark_safe("<a href='/blog/preview/%s'>Preview</a>" % obj.id)
    
    preview_post.allow_tags = True
    preview_post.short_description = 'Preview Post'
    
    search_fields = ["title"]
    display_fields = ["title", "created"]
    list_display = ('title', 'created', "visible" , "preview_post")
    prepopulated_fields = {"slug" : ("title",)}

