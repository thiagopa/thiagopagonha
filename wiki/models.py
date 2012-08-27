from django.db import models
from django.contrib import admin

class Page(models.Model):
    name = models.CharField(max_length=60)
    
    data = models.TextField()
    
    def __unicode__(self):
        return self.name
    
admin.site.register(Page)    