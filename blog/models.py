from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

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
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    
    short_description = models.CharField(max_length=60)

    views_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    
    objects = PostManager()
    
    @models.permalink
    def get_absolute_url(self):
        return ('blog', [self.slug])


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
    search_fields = ["title"]
    display_fields = ["title", "created"]
    filter_horizontal = ('categories',)
    list_display = ('title', 'created')
    prepopulated_fields = {"slug" : ("title",)}

