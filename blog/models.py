from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.mail import send_mail

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

    objects = PostManager()
    
    @models.permalink
    def get_absolute_url(self):
        return ('single_post', [self.slug])


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
        

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))

    def save(self, *args, **kwargs):
        """Email when a comment is added."""
        if "notify" in kwargs and kwargs["notify"] == True:
            message = "Comment was added to '%s' by '%s': \n\n%s" % (self.post,self.author,self.body)
            from_addr = "thiagopagonha@appspot.gserviceaccount.com"
            recipient_list = ["thi.pag@gmail.com"]
            send_mail("New comment added", message, from_addr, recipient_list)

        if "notify" in kwargs: del kwargs["notify"]
        super(Comment, self).save(*args, **kwargs)


### Admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    display_fields = ["title", "created"]
    filter_horizontal = ('categories',)
    list_display = ('title', 'created')
    prepopulated_fields = {"slug" : ("title",)}

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]
