from django.db import models
from django.contrib import admin

class Page(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    
    data = models.TextField()
    
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
admin.site.register(Page)    